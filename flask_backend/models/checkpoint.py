from app import db

class CheckPoint(db.Model):
    __tablename__ = 'checkpoint'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    status = db.Column(db.Boolean)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event = db.relationship('Event', backref='checkpoints', uselist=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group')
