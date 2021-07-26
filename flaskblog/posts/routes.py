from bs4 import BeautifulSoup as soup
from flask import Blueprint, flash, redirect, url_for, render_template, abort, \
    request
from flask_login import login_required, current_user
from  bs4 import BeautifulSoup
import requests
from flaskblog import db
from flaskblog.models import Post, User
from flaskblog.posts.forms import PostForm
from elasticsearch import Elasticsearch
from requests import get


posts = Blueprint('posts', __name__)


@posts.route('/posts/Kannada')
def kannada_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(language='Kannada').paginate(per_page=15, page=page)
    
    return render_template('kannada.html', posts=posts, title='Kannada', num_registered=User.get_num_registered())


@posts.route('/posts/Hindi')
def hindi_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Hindi').paginate(per_page=15, page=page)
    return render_template('hindi.html', posts=posts, title='Hindi', num_registered=User.get_num_registered())


@posts.route('/posts/Telugu')
def telugu_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Telugu').paginate(per_page=15, page=page)
    return render_template('telugu.html', posts=posts, title='Telugu', num_registered=User.get_num_registered())


@posts.route('/posts/Tamil')
def tamil_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Tamil').paginate(per_page=15, page=page)
    return render_template('tamil.html', posts=posts, title='Tamil', num_registered=User.get_num_registered())


@posts.route('/posts/Italian')
def italian_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Italian').paginate(per_page=15, page=page)
    return render_template('italian.html', posts=posts, title='Italian', num_registered=User.get_num_registered())


@posts.route('/posts/German')
def german_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='German').paginate(per_page=15, page=page)
    return render_template('german.html', posts=posts, title='German', num_registered=User.get_num_registered())


@posts.route('/posts/Danish')
def danish_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Danish').paginate(per_page=15, page=page)
    return render_template('danish.html', posts=posts, title='Danish', num_registered=User.get_num_registered())


@posts.route('/posts/French')
def french_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='French').paginate(per_page=15, page=page)
    return render_template('french.html', posts=posts, title='French', num_registered=User.get_num_registered())



@posts.route('/posts/Russian')
def russian_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Russian').paginate(per_page=15, page=page)
    return render_template('russian.html', posts=posts, title='Russian', num_registered=User.get_num_registered())


@posts.route('/posts/English')
def english_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='English').paginate(per_page=15, page=page)
    return render_template('english.html', posts=posts, title='English', num_registered=User.get_num_registered())


@posts.route('/posts/Swedish')
def swedish_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Swedish').paginate(per_page=15, page=page)
    return render_template('swedish.html', posts=posts, title='Swedish', num_registered=User.get_num_registered())


@posts.route('/posts/Spanish')
def spanish_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Spanish').paginate(per_page=15, page=page)
    return render_template('spanish.html', posts=posts, title='Spanish', num_registered=User.get_num_registered())


@posts.route('/posts/Malayalam')
def malyalam_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Malayalam').paginate(per_page=15, page=page)
    return render_template('malyalam.html', posts=posts, title='Malayalam', num_registered=User.get_num_registered())

@posts.route('/posts/Japanese')
def japanese_post():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(
        language='Japanese').paginate(per_page=15, page=page)
    return render_template('japanese.html', posts=posts, title='Japanese', num_registered=User.get_num_registered())


@posts.route('/post/<string:post_title>', methods=['GET', 'POST'])
def post(post_title):
    post_object2 = Post.query.filter_by(title=post_title).first_or_404()
    return render_template('post.html',
                           post=post_object2,
                           num_registered=User.get_num_registered())

@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post_object = Post.query.get_or_404(post_id)
    if post_object.author != current_user:
        abort(403)
    post_form = PostForm()
    if post_form.validate_on_submit():
        post_object.imdb_id = post_form.imdb_id.data
        post_object.title = post_form.title.data
        post_object.overview = post_form.overview.data
        post_object.budget = post_form.budget.data
        post_object.revenue = post_form.revenue.data
        post_object.geners = post_form.geners.data
        post_object.language = post_form.language.data
        post_object.runtime = post_form.runtime.data
        post_object.release_date = post_form.release_date.data
        post_object.vote_average = post_form.vote_average.data
        post_object.vote_count = post_form.vote_count.data
        post_object.country = post_form.country.data
        post_object.year = post_form.year.data
        post_object.director = post_form.director.data
        post_object.writer = post_form.writer.data
        post_object.production = post_form.production.data
        post_object.actor = post_form.actor.data
        db.session.commit()
        flash('Post was updated', 'success')
        return redirect(url_for('posts.post', post_id=post_object.id,post_title=post_object.title))
    elif request.method == 'GET':
        post_form.imdb_id.data = post_object.imdb_id
        post_form.title.data = post_object.title
        post_form.overview.data = post_object.overview
        post_form.budget.data = post_object.budget
        post_form.revenue.data = post_object.revenue
        post_form.geners.data = post_object.geners
        post_form.language.data = post_object.language
        post_form.runtime.data = post_object.runtime
        post_form.release_date.data = post_object.release_date
        post_form.vote_average.data = post_object.vote_average
        post_form.vote_count.data = post_object.vote_count
        post_form.country.data = post_object.country
        post_form.year.data = post_object.year
        post_form.director.data = post_object.director
        post_form.writer.data = post_object.writer
        post_form.production.data = post_object.production
        post_form.actor.data = post_object.actor
    return render_template('create_post.html', title='Update Post',
                           form=post_form, legend='Update Post',
                           num_registered=User.get_num_registered())


@posts.route('/post/<string:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post_object = Post.query.get_or_404(post_id)
    if post_object.author != current_user:
        abort(403)
    db.session.delete(post_object)
    db.session.commit()
    flash('Post was deleted', category="success")
    return redirect(url_for('main.language'))



