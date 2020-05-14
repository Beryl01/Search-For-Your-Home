from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, IntegerField,SelectField,FileField
from wtforms.validators import Required
from flask_wtf.file import FileField, FileAllowed,FileRequired
from flask_uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)





class PropertyForm(FlaskForm):

    description = TextAreaField('Describe your property', validators=[Required()])
    location = SelectField('Location', choices=[('nairobi', 'nairobi'), ('mombasa', 'mombasa'), ('kisumu', 'kisumu')],
                           validators=[Required()])

    rent = IntegerField('Rent amount', validators=[Required()])

    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])

    submit = SubmitField('Post')
    