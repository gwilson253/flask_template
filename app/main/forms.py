from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, Length
#from wtforms import ValidationError
#from flask_pagedown.fields import PageDownField
#from ..models import User, Role

class TestEmailForm(Form):
    email = StringField('Test Email', validators=[Required(), Length(1, 64), 
                                             Email()])
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Run Test')

class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')