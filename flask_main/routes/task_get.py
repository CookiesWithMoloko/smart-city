from app import task_api
from flask import jsonify
from models.task import Task


@task_api.route('/get/')
def get():
    i: Task
    return jsonify(dict(
        status=True,
        result=[
            dict(id=i.id,
                 name=i.name,
                 description=i.description,
                 events=[dict(
                     id=j.id,
                     name=j.name,
                     start=j.start,
                     end=j.end
                 ) for j in i.events]
                 ) for i in Task.query.all()
        ]
    ))
