
from flask import Flask
from flask_ckeditor import CKEditor

app = Flask(__name__)

ckeditor = CKEditor(app)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinkup_database.db'
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from views import *
#app.run(debug=False)