from typing import Optional
class AuthApiUser:
    pass


class AuthApiUser:
    def __init__(self, token: str):
        """

        :param token: Токен авторизации
        """
        pass
    def is_authorized(self) -> bool:
        pass
    def is_admin(self) -> bool:
        pass
    def get_group(self) -> int:
        pass
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
    def register(self, email: str, name: str) -> int:
        """

        :param self:
        :param email: Почта
        :param name: Имя человека
        :return: id зарегистрированного пользователя
        """
        pass
    @staticmethod
    def auth(self, email: str, password: str) -> Optional[AuthApiUser]:
        """

        :param self:
        :param email: Почта
        :param password: Пароль
        :return: Зарегистрированный пользователь или None
        """
        pass
