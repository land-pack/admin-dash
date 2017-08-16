import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
import flask_login as login
import flask_admin as admin
from config import basedir

lm = LoginManager()

app = Flask(__name__)
app.config.from_object("config")

# Create dummy secrey key so we can use sessions
#app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
#app.config['DATABASE_FILE'] = 'sample_db.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
#app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
db = SQLAlchemy(app)




"""
If you are wondering why the import statement is at the end and not at 
the beginning of the script as it is always done, the reason is to avoid 
circular references, because you are going to see that the views module 
needs to import the app variable defined in this script. Putting the 
import at the end avoids the circular import error.
"""
from core import views, models


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(models.User).get(user_id)


# Initialize flask-login
init_login()
