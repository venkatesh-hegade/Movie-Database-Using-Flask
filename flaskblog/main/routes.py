

from flask import Blueprint, request, render_template,redirect,g
from flask import Blueprint, flash, redirect, url_for, render_template, abort, \
    request



from flaskblog.models import User, Post


from flaskblog.models import Post, User
from flask import current_app
main = Blueprint('main', __name__)



@main.route('/')
def home():
    return render_template('home.html')


@main.route('/language')
def language():
    return render_template('language.html')




