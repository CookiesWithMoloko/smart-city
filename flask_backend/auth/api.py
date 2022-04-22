class AuthApiUser:
    pass


class AuthApiUser:
    def __init__(self, token: str):
        pass
    def is_authorized(self) -> bool:
        pass
    def is_admin(self) -> bool:
        pass
    def get_group(self) -> int:
        pass
    def get_token(self) -> str:
        pass
    def __bool__(self):
        return self.is_authorized()
    def __str__(self):
        pass
    @staticmethod
    def register(self, email: str) -> int:
        pass
    @staticmethod
    def auth(self, email: str, password: str) -> AuthApiUser:
        pass
