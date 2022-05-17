from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    username = StringField('username', validators =[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password1 = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password1')])
    submit = SubmitField('Register')