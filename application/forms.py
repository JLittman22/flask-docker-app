from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class UserForm(Form):
    userid = StringField('openid')
