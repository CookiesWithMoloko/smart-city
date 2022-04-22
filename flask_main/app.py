from flask import Flask, Blueprint
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


def as_dict(self):
    r = dict()

    def get(name: str):

        a = getattr(self, name)
        if isinstance(a, db.Model):
            r[name] = a.as_dict()
        else:
            r[name] = a
    for c in self.__table__.columns:
        get(c.name)
    for c in [str(i.class_attribute).split('.')[-1] for i in list(self.__mapper__.relationships)]:
         get(c)
    return r
db.Model.as_dict = as_dict
api = Blueprint('api', __name__)
task_api = Blueprint('tasks', __name__)
event_api = Blueprint('events', __name__)

