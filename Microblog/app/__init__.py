from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from flask_login import LoginManager
from flask_openid import OpenID
import flask_openid
import os


app = Flask(__name__)
app.config.from_object('config')




db = SQLAlchemy(app)
from models import User, Post
db.create_all()
db.session.commit()



lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))




from app import views, models
