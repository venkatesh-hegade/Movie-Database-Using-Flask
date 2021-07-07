from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,IntegerField,TextField,FloatField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    imdb_id = StringField('IMDB ID')
    title = StringField('Title', validators=[DataRequired()])
    overview = TextAreaField('Overview', validators=[DataRequired()])
    budget = IntegerField('Budget')
    revenue = IntegerField('Revenue')
    geners = TextField('Gener')
    language = StringField('Language')
    runtime = IntegerField('Runtime')
    release_date = StringField('Release Date')
    vote_average = FloatField('Vote Average')
    vote_count = IntegerField('Vote Count')
    country = StringField('Country Origin')
    year = IntegerField('Year')
    director = StringField('Director')
    writer = StringField('Writer')
    production = StringField('Production')
    actor = StringField('Actor')
    submit = SubmitField('Submit')


