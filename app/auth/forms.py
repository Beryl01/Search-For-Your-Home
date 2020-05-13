from flask_babel import lazy_gettext
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError, BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo



class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class LoginOwnerForm(FlaskForm):
    email = StringField(lazy_gettext('Email'), validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(lazy_gettext('Password'), validators=[DataRequired()])
    remember_me = BooleanField(lazy_gettext('Keep me logged in'))
    submit = SubmitField(lazy_gettext('Log in'))


class RegistrationOwnerForm(FlaskForm):
    email = StringField(lazy_gettext('Email'), validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(lazy_gettext('Username'), validators=[
        DataRequired(), Length(1, 32), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, lazy_gettext(
            'Usernames must have only letters, numbers, dots or underscores'))])
    password = PasswordField(lazy_gettext('Password'), validators=[
        DataRequired(), EqualTo('password2', message=lazy_gettext('Passwords must match.'))])
    password2 = PasswordField(lazy_gettext('Confirm password'), validators=[DataRequired()])
    submit = SubmitField(lazy_gettext('Register'))

