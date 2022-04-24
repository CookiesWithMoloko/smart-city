from app import app
from api import GlobalApi
from models.group import Group
from models.task import Task
from models.event import Event
from models.checkpoint import CheckPoint
from flask import render_template
@app.route('/agency')
def agency():
    api = GlobalApi(None)
    name = api.user.get_full_info()['name']
    group_name = Group.query.filter_by(id=api.user.get_group()).first().name
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
                start=check.start,
                end=check.end,
                group_name=check.group.name
            ) for check in event.checkpoints if check.group_id == api.user.get_group()]
        ) for event in task.events]
    ) for task in r]
    return render_template('agency.html',
                           name=name,
                           group_name=group_name,
                           tasks=r)
