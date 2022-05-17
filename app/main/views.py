from . import auth
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,logout_user,login_required,current_user
from ..models import User
from flask import redirect,render_template,url_for,flash,request
from .. import db


@auth.route('/register', methods = ['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username =form.username.data, email = form.email.data,password=form.password1.data)
            # user.set_password(form.password1.data)
            user.save()
            return redirect(url_for('auth.login'))
        else:
            flash('That username is in use try a new one')
    return render_template('auth/signup.html', form=form)