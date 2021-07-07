import time
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadData
from flask import current_app
from flask_login import UserMixin
from flaskblog import db, login_manager


# from flaskblog.remainders import utils

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    reviews = db.relationship('Review', backref='user_post', lazy=True)
   
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @classmethod
    def get_num_registered(cls):
        return cls.query.count()

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except BadData:
            return None
        return user_id

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    __tablename__ = 'post'
    __searchable__ =['id','title']
    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    budget = db.Column(db.Integer)
    revenue = db.Column(db.Integer)
    geners = db.Column(db.Text)
    language = db.Column(db.String)
    runtime = db.Column(db.Integer)
    release_date = db.Column(db.String)
    vote_average = db.Column(db.Float)
    vote_count = db.Column(db.Integer)
    country = db.Column(db.String)
    year = db.Column(db.Integer)
    director = db.Column(db.String)
    writer = db.Column(db.String)
    production = db.Column(db.String)
    actor = db.Column(db.String)
    reviews = db.relationship('Review', backref='author', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.overview}')"


class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))
 

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"







