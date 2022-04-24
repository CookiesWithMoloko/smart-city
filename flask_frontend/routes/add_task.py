from app import app, db
from flask import request, abort, redirect, url_for
from datetime import datetime
from models.task import Task
from models.group import Group
from models.event import Event
from models.checkpoint import CheckPoint
@app.post('/add_task')
def add_task():
    task = request.form.get('task', None)
    event = request.form.get('event', None)
    checkpoint = request.form.get('checkpoint', None)
    group = request.form.get('group', None)
    # 2022-04-27
    # %Y-%m-%d
    start = request.form.get('start', None, lambda a: datetime.strptime(a, '%Y-%m-%d'))
    end = request.form.get('end', None, lambda a: datetime.strptime(a, '%Y-%m-%d'))
    if None in [task, event, checkpoint, group, start, end]:
        return abort(400)
    t = Group.query.filter_by(name=group).first()
    if t is None:
        group = Group(name=group)
        db.session.add(group)
        group = Group.query.filter_by(name=group.name).first()
    else:
        group = t
    t = Task.query.filter_by(name=task).first()
    if t is None:
        task = Task(name=task)
        db.session.add(task)
        task = Task.query.filter_by(name=task.name).first()
    else:
        task = t
    t = Event.query.filter_by(name=event).first()
    if t is None:
        event = Event(name=event, task_id=task.id)
        db.session.add(event)
        event = Event.query.filter_by(name=event.name).first()
    else:
        event = t
    t = CheckPoint.query.filter_by(name=checkpoint).first()
    if t is None:
        checkpoint = CheckPoint(
            name=checkpoint,
            event_id=event.id,
            group_id=group.id,
            start=start,
            end=end,
            status=0
        )
        db.session.add(checkpoint)
        checkpoint = CheckPoint.query.filter_by(name=checkpoint.name)
    else:
        return abort(400)
    db.session.commit()
    return redirect(url_for('.admin'))
