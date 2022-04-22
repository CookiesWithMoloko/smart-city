from app import task_api
from flask import jsonify
from models.task import Task

@task_api.route('/get/')
def get():
    i: Task
    return jsonify(dict(
        status=True,
        result=[
            i.as_dict() for i in Task.query.all()
        ]
    ))
