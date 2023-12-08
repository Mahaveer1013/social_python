from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class login(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    username= db.Column(db.String(150), nullable=False)
    password= db.Column(db.String(150), nullable=False)
    email= db.Column(db.String(150), nullable=False)
    dp_name= db.Column(db.String(150), nullable=False)
    #dp_mimetype= db.Column(db.String(150), nullable=False)



class post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Integer)
    post_msg = db.Column(db.String(150), nullable=False)
    post_name = db.Column(db.String(150), nullable=False)
    #post_mimetype = db.Column(db.String(150), nullable=False)
    post_path = db.Column(db.String(150), nullable=False)

