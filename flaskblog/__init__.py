
from flask import Flask,request
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_executor import Executor
from flask_babel import Babel
from flask import current_app

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
executor = Executor()

login_manager = LoginManager()
login_manager.login_view = 'users.login'  # function name of login route
login_manager.login_message_category = 'info'  # bootstrap class for messages

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.reviews.routes import reviewss
from flaskblog.errors.handlers import errors


def create_app():
    print("create app")
    app = Flask(__name__)
    app.config['ELASTICSEARCH_URL'] = 'http://127.0.0.1:5000'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = ''
    app.config['MAIL_PASSWORD'] = ''
    app.config['EXECUTOR_TYPE'] = 'thread'
    app.config['POSTS_PER_PAGE'] = 25
    mail=Mail(app)
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
  
    login_manager.init_app(app)
    executor.init_app(app)
    
  

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(reviewss)
    return app
  





