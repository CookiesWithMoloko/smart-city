from app import atc
from api import GlobalApi
from flask import request, jsonify
from models.chat import Chat


@atc.route('get_chats')
def get_chats():
    api = GlobalApi(request.cookies.get('token', None))
    if not api.user.is_authorized():
        return jsonify(dict(
            status=False,
            error='Чаты доступны только авторизованным пользователям'
        )), 400
    group = api.user.get_group()
    chats = Chat.query.filter_by(group_id=group).all()
    i: Chat
    return jsonify(dict(
        status=True,
        chats=[dict(
            task=api.task.get_task(i.task_id)
        ) for i in chats]
    ))
