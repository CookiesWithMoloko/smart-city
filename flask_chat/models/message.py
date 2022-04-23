from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)