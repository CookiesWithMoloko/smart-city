from app import atc, app
__import__('utils').import_dir('routes')
app.register_blueprint(atc, url_prefix='/attachments')
