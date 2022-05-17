from . import auth
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,logout_user,login_required,current_user
from ..models import User
from flask import redirect,render_template,url_for,flash,request
from .. import db