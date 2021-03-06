from typing import Optional
from models.user import User
class AuthApiUser:
    pass


class AuthApiUser:
    def __init__(self, token: str):
        self.data: User = User.query.filter_by(id=1).first()
        self.data = dict(
            id=self.data.id,
            name=self.data.name,
            group=dict(
                name=self.data.group[0].name,
                id=self.data.group[0].id,
                admin=self.data.group[0].admin
            )
        )
        """

        :param token: Токен авторизации
        """
        pass
    def get_full_info(self) -> dict:
        return self.data
    def is_authorized(self) -> bool:
        return True
    def is_admin(self) -> bool:
        return self.data['admin']
    def get_group(self) -> int:
        return self.data['group']['id']
    def get_token(self) -> str:
        """

        :return: Токен авторизации
        """
        pass
    def __bool__(self):
        return self.is_authorized()
    def __str__(self):
        pass
    @staticmethod
    def register(email: str, name: str) -> int:
        """

        :param email: Почта
        :param name: Имя человека
        :return: id зарегистрированного пользователя
        """
        pass
    @staticmethod
    def auth(email: str, password: str) -> Optional[AuthApiUser]:
        """

        :param email: Почта
        :param password: Пароль
        :return: Зарегистрированный пользователь или None
        """
        pass
