from app import app
from flask import request

@app.post('/edit_checkpoints')
def edit_check():
    check_id = request.args.get('check_id')
    name = request.args.get('name')
    group = request.args.get('group')


