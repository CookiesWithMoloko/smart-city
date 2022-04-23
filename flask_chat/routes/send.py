from flask import request, jsonify
from app import atc, db
from api import GlobalApi
from models.chat import Chat
from models.message import Message
@atc.route('send')
def send():
    chat_id = request.args.get('chat_id', None, int)
    content = request.args.get('content', '', str)
    attachment = request.args.get('attachment_id', None, int)
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
            != api.task.get_task(chat.task_id)['group_id']) \
            and not api.user.is_admin():
        return jsonify(dict(
            status=False,
            error='У вас нет прав на отправку сообщений в данный чат'
        )), 400
    attachment_link = api.attachments.get_attachment(attachment)
    if attachment_link is None:
        return jsonify(dict(
            status=False,
            error='Ошибка при загрузке вложения'
        )), 400
    db.seession.add(
        Message(
            author_id=api.user.get_full_info()['id'],
            content=content,
            attachment_id=attachment,
            chat_id=chat_id
        )
    )
    db.session.commit()
    return jsonify(dict(
        status=True
    ))



