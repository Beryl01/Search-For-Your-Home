from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, IntegerField,SelectField
from wtforms.validators import Required




class PropertyForm(FlaskForm):
    title = StringField('Property name', validators=[Required()])
    location = SelectField('Location', choices=[('nairobi', 'nairobi'), ('mombasa', 'mombasa'), ('kisumu', 'kisumu')],
                           validators=[Required()])

    rent = IntegerField('Rent amount', validators=[Required()])
    submit = SubmitField('Post')