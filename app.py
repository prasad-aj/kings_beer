
from flask import Flask
from flask_ckeditor import CKEditor

app = Flask(__name__)

ckeditor = CKEditor(app)

#app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kb_database.db'
#app.config ['SQLALCHEMY_DATABASE_URI'] = "postgres://iemxmqrjobuxvu:be1b8f329726d4478dc27c5bfd008ab9526ddc7762addcfc64c520be87c53042@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d2nrufs17nn2ms"
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgres://iemxmqrjobuxvu:be1b8f329726d4478dc27c5bfd008ab9526ddc7762addcfc64c520be87c53042@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d2nrufs17nn2ms'

app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from views import *
#app.run(debug=False)
