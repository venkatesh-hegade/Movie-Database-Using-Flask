from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import current_user, login_user, logout_user, login_required

from flaskblog import bcrypt, db
from flaskblog.models import User, Post 
from flaskblog.users.forms import RegistrationForm, LoginForm, \
    UpdateAccountForm
from flaskblog.users.utils import save_picture

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.language'))
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            register_form.password.data).decode('utf-8')
        user = User(username=register_form.username.data,
                    email=register_form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {register_form.username.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register',
                           form=register_form,
                           num_registered=User.get_num_registered())


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.language'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('language')
        else:
            flash(f'Check email or password', 'danger')
    return render_template('login.html', title='Login', form=login_form,
                           num_registered=User.get_num_registered())


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    update_account_form = UpdateAccountForm()
    if request.method == 'GET':
        update_account_form.username.data = current_user.username
        update_account_form.email.data = current_user.email
    elif update_account_form.validate_on_submit():
        if update_account_form.picture.data:
            picture_file = save_picture(update_account_form.picture.data)
            current_user.image_file = picture_file
        current_user.username = update_account_form.username.data
        current_user.email = update_account_form.email.data
        db.session.commit()
        flash('your account has been updated', 'success')
        return redirect(url_for('users.account'))
    image_file = url_for('static', filename='profile_pics/' +
                                            current_user.image_file)
    return render_template('account.html',
                           title='Account',
                           image_file=image_file,
                           form=update_account_form,
                           num_registered=User.get_num_registered()
                           )


@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(
        Post.release_date.desc()).paginate(per_page=4, page=page)
    return render_template('user_posts.html', posts=posts, user=user,
                           num_registered=User.get_num_registered())









