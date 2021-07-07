import os
import secrets

from PIL import Image
from flask import url_for, current_app
from flask_mail import Message




def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path,'static/profile_pics', picture_fn)
    output_image_size = (125, 125)
    resized_img = Image.open(form_picture)
    resized_img.thumbnail(output_image_size)
    resized_img.save(picture_path)
    return picture_fn


