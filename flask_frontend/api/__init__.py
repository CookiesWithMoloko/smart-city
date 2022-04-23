from api.auth import AuthApiUser
from api.attach import AttachmentApi
from api.task import TaskApi
class GlobalApi:
    def __init__(self, token: str):
        self.attachments = AttachmentApi(token)
        self.user = AuthApiUser(token)
        self.task = TaskApi(token)
