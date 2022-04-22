from flask import request, jsonify
from app import task_api, db
from models.task import Task
from auth.api import AuthApiUser

@task_api.route('/create/')
def create():
    token = request.cookies.get('token', None)
    if not AuthApiUser(token).is_admin():
        name = request.args.get('name', None)
        description = request.args.get('description', None)
        if name is None:
            return jsonify(dict(
                status=False,
                error='Не указано название задания <name>'
            )), 400
        db.session.add(Task(
            name=name,
            description=description
        ))
        db.session.commit()
        return jsonify(dict(
            status=True,
            id=Task.query.filter_by(name=name).first().id
        ))
