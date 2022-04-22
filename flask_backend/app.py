from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder='static')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.url_map.strict_slashes = False
app.secret_key = os.urandom(24)
db = SQLAlchemy(app)
