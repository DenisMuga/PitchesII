from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstraps import Bootstrap  
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()
from app.models import User,Blog,Comment,Subscriber
mail = Mail()
bootstap = Bootstrap()
