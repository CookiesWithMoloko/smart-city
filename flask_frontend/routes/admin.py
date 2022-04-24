from app import app
from flask import render_template
from models.task import Task
from models.event import Event
from models.checkpoint import CheckPoint
@app.route('/admin')
def admin():
    r = Task.query.all()
    task: Task
    event: Event
    check: CheckPoint
    r = [dict(
        name=task.name,
        events=[dict(
            name=event.name,
            checkpoints=[dict(
                id=check.id,
                name=check.name,
                start=check.start,
                end=check.end,
                group_name=check.group.name
            ) for check in event.checkpoints]
        ) for event in task.events]
    ) for task in r]
    return render_template('admin.html', tasks=r)
