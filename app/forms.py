from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField
# other fields include PasswordField
from wtforms.validators import Required, Email

class SendForm(Form):
    name = TextField('Name', validators=[Required()])
    email = TextField('Email', validators=[Required(), Email()])
    subject = TextField('Subject', validators=[Required()])
    comments = TextAreaField('Message', validators=[Required()])
    submit = SubmitField('Send')