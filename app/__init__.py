from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
#from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
db_path = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(db_path, 'database.db'))
db = SQLAlchemy(app)
socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.login_view = 'views.user_login'
login_manager.init_app(app)

UPLOAD_DP = os.path.join(app.root_path, 'static\img\dp')
app.config['UPLOAD_DP'] = UPLOAD_DP
UPLOAD_POST = os.path.join(app.root_path, 'static\img\post')
app.config['UPLOAD_POST'] = UPLOAD_POST

@login_manager.user_loader
def load_user(id):
    return login.query.get(int(id))

from .models import login,post

with app.app_context():
    db.create_all()
    print("Database Created")

from app import views