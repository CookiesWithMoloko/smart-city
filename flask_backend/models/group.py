from app import db

class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    admin = db.Column(db.Boolean, default=False)
