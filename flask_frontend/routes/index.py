from app import app
from flask import render_template
from models.task import Task
from models.event import Event
from models.checkpoint import CheckPoint
@app.route('/')
@app.route('/index')
def index():
    r = Task.query.all()
    task: Task
    event: Event
    check: CheckPoint
    r = [dict(
        name=task.name,
        events=[dict(
            name=event.name,
            checkpoints=[dict(
                name=check.name,
                group_name=check.group.name
            ) for check in event.checkpoints]
        ) for event in task.events]
    ) for task in r]
    return render_template('index.html', tasks=r)
