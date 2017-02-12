from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
from app import views


app.config['DEBUG'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['DEFAULT_MAIL_SUBJECT'] = '[User def]'
app.config['DEFAULT_MAIL_SENDER'] = 'Admin <admin@example.com>'
app.config['SECRET_KEY'] = 'mys3cr3tk3y'
app.config['DEFAULT_ADMIN'] = 'Admin <admin@example.com>'

CSRFProtect(app)
