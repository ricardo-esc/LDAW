from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask import session
import flaskpdf
from flask_qrcode import QRcode


app = Flask(__name__)

app.secret_key = "hello"
flaskpdf.init_app(app)
QRcode(app)


from main import routes

