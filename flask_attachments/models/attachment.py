from app import db
from sqlalchemy.sql import func
class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    path = db.Column(db.String(256), unique=True)
    time = db.Column(db.DateTime, server_default=func.now())
    author = db.Column(db.Integer, nullable=True)
