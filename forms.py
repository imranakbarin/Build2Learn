from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    UserName=StringField('UserName', validators=[DataRequired()])
    Password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

class RegistrationForm(FlaskForm):
    FirstName=StringField('FirstName', validators=[DataRequired()])
    LastName=StringField('LastName', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired()])
    PhoneNumber=StringField('PhoneNumber', validators=[DataRequired()])
    Password=PasswordField('Password', validators=[DataRequired()])
    ConfirmPassword=PasswordField('ConfirmPassword', validators=[DataRequired(), EqualTo('Password')])
   
    submit=SubmitField('Register')

