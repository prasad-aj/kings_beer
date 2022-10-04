
from flask import Flask
from flask_ckeditor import CKEditor

app = Flask(__name__)

ckeditor = CKEditor(app)
#app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kb_database.db'
app.config ['SQLALCHEMY_DATABASE_URI'] = "postgresql://dmdnnldxytlymm:a781e6be17ff9ef4d187f13ab3e1ca3a4adb4f8396cb630a3084feb85da392ab@ec2-23-21-207-93.compute-1.amazonaws.com:5432/ddk6ofdttpdjdm"

app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from views import *
#app.run(debug=False)