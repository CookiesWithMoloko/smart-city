from app import atc, app, db
from flask import request, abort, jsonify
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from auth.api import AuthApiUser
from models.attachment import Attachment
from hashlib import md5
import os
FILE_EXTENSIONS = set(
    'txt', 'pdf',
    'doc', 'dot', 'wbk',
    'docx', 'docm', 'dotx', 'dotm', 'docb',
    'wll', 'wwl',
    'png', 'jpg', 'jpeg',
    'webm', 'mkv', 'mp3', 'mp4',
    'vob', 'ogg', 'avi', 'mov',
    'mpg', 'mpeg'
)
@atc.route('/add')
def add():
    user = AuthApiUser(request.cookies.get('token'))
    r = []
    file: FileStorage
    if 'file' not in request.files:
        return abort(400)
    file = request.files['file']
    if file.rsplit('.', 1)[1].lower() not in FILE_EXTENSIONS:
        return abort(400)
    filename = secure_filename(file.filename)

    tid = -1
    if user.is_authorized():
        tid = user.get_full_info()['id']
    filename = f'{md5(str(tid).encode()).hexdigest()}.{filename}'
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)
    db.session.add(Attachment(
        name=filename,
        path=path,
        author=tid
    ))
    db.session.commit()
    r = Attachment.query.filter_by(path=path).first()
    return jsonify(dict(
        status=True,
        id=r.id
    ))

