from flask import request, jsonify
from app import atc
from api import GlobalApi
from models.chat import Chat
from datetime import datetime

@atc.route('get')
def get():
    chat_id = request.args.get('chat_id', None, int)
    time = request.args.get('time', 0, int)
    offset = request.args.get('offset', 0, int)
    time = datetime.utcfromtimestamp(time)
    chat = Chat.query.filter_by(id=chat_id).first()
    api = GlobalApi(request.cookies.get('token', None))
    if not api.user.is_authorized():
        return jsonify(dict(
            status=False,
            error='Доступ разрешен только авторизованным пользователям'
        )), 400
    if chat is None:
        return jsonify(dict(
            status=False,
            error='Данного чата не существует'
        )), 400

    if (api.user.get_full_info()['group_id']
            != api.task.get_task(chat.task_id)['group_id'])\
            and not api.user.is_admin():
        return jsonify(dict(
            status=False,
            error='У вас нет прав на просмотр данного чата'
        )), 400
    return jsonify(dict(
        status=True,
        result=list(sorted(
            list(filter(lambda a: a.time >= time, chat.messages))
        ), lambda a: a.time)[offset * 50:(offset+1)*50],
        messages_count=len(chat.messages)
    ))

