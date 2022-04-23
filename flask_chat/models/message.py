from app import db
from sqlalchemy.sql import func


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, server_default=func.now())
    content = db.Column(db.Text)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    chat = db.relationship('Chat', backref='messages', uselist=True)
    attachment_id = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer)
