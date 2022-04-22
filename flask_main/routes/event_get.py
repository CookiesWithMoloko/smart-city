from app import event_api
from flask import jsonify, request
from models.task import Task
from models.event import Event
from models.checkpoint import CheckPoint
@event_api.route('/get')
def get():
    task_id = request.args.get('task_id', None, int)
    event_id = request.args.get('event_id', None, int)
    if task_id is None and event_id is None:
        return jsonify(dict(
            status=False,
            error='Все аргументы пусты <task_id>, <event_id>'
        )), 400
    if event_id is not None:
        i: Event
        j: CheckPoint
        return jsonify(dict(
            status=True,
            result=[dict(
                id=i.id,
                name=i.name,
                start=i.start,
                end=i.end,
                task_id=i.task_id,
                checkpoints=[dict(
                    name=j.name,
                    event_id=j.event_id,
                    group=dict(
                        id=j.group.id,
                        name=j.group.name
                    )
                ) for j in i.checkpoints]
            ) for i in Event.query.all()]
        ))
    i: Task
    j: Event
    return jsonify(dict(
        status=True,
        result=[dict(
            id=i.id,
            name=i.name,
            description=i.description,
            events=[dict(
                id=j.id,
                name=j.name,
                start=j.start,
                end=j.end
            ) for j in i.events]
        ) for i in Task.query.filter_by(id=task_id).all()]
    ))
