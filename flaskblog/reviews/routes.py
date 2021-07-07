from flask import Blueprint, flash, redirect, url_for, render_template, abort, \
    request
  
from flask_login import login_required, current_user
from flaskblog import db
from flaskblog.models import Review, User,Post
from flaskblog.reviews.forms import ReviewForm


reviewss = Blueprint('reviews', __name__)


@reviewss.route('/post/<int:post_id>/new_review', methods=['GET', 'POST'])
@login_required
def new_review(post_id):
    review_form = ReviewForm()
    post = Post.query.get_or_404(post_id)
    if review_form.validate_on_submit():
        review = Review(title=review_form.title.data, content=review_form.content.data,author=post,
                        user_post=current_user)
        db.session.add(review)
        db.session.commit()
        flash('Review was created', 'success')
        return redirect(url_for('reviews.review',post_id=post.id,review_id=review.id))
    return render_template('create_review.html', title='New Review',
                           form=review_form, legend='New Review',
                           num_registered=User.get_num_registered())

@reviewss.route('/post/<int:post_id>/review')
def all_reviews(post_id):
    post = Post.query.get_or_404(post_id)

    page = request.args.get('page', 1, type=int)
    reviews = Review.query.filter_by(author=post).order_by(Review.date_posted.desc()).paginate(per_page=4, page=page)
    return render_template('reviews.html',posts=post,reviews=reviews,post=post,
                           num_registered=User.get_num_registered())


@reviewss.route('/post/<int:post_id>/<int:review_id>/review', methods=['GET', 'POST'])
def review(post_id,review_id):
    post_object = Post.query.get_or_404(post_id)
    review_object = Review.query.get_or_404(review_id)
    return render_template('review.html',post=post_object,review=review_object,num_registered =User.get_num_registered)
    


@reviewss.route('/user/review/<string:username>',methods=['GET','POST'])
def user_reviews(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    reviews = Review.query.filter_by(user_post=user).order_by(Review.date_posted.desc()).paginate(per_page=5,page=page)
    
    return render_template('user_reviews.html',reviews=reviews,user=user,
                           num_registered=User.get_num_registered())

@reviewss.route('/post/<int:post_id>/<int:review_id>/review/update', methods=['GET', 'POST'])
@login_required
def update_review(post_id,review_id):
    post_object = Post.query.get_or_404(post_id)
    review_object = Review.query.get_or_404(review_id)
    if review_object.user_post != current_user:
        abort(403)
    review_form = ReviewForm()
    if review_form.validate_on_submit():
        review_object.title = review_form.title.data
        review_object.content = review_form.content.data
        db.session.commit()
        flash('Post was updated', 'success')
        return redirect(url_for('reviews.review', post_id=post_object.id,review_id=review_object.id))
    elif request.method == 'GET':
        review_form.title.data = review_object.title
        review_form.content.data = review_object.content
    return render_template('create_review.html', title='Update Review',
                           form=review_form, legend='Update Review',
                           num_registered=User.get_num_registered())


