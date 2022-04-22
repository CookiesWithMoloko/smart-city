from app import api, app, task_api, event_api

__import__('utils').import_dir('routes')

api.register_blueprint(task_api, url_prefix='/tasks')
api.register_blueprint(event_api, url_prefix='/events')
app.register_blueprint(api, url_prefix='/api')
