from flask import request, jsonify, send_file

from app import atc
from auth.api import AuthApiUser
from models.attachment import Attachment


@atc.route('/get')
def get():
    r = request.args.get('id', -1, int)
    user = AuthApiUser(request.cookies.get('token'))
    att: Attachment = Attachment.query.filter_by(id=r).first()
    if att is None:
        return jsonify(dict(
            status=False,
            error='Файл с таким id не найден'
        )), 400
    if att.author == user.get_full_info()['id'] or att.author == -1 or user.is_admin():
        return send_file(att.path, as_attachment=True)
    return jsonify(dict(
        status=False,
        error='У вас недостаточно прав для доступа к этому файлу'
    )), 400


