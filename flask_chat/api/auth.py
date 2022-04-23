from typing import Optional
class AuthApiUser:
    pass


class AuthApiUser:
    def __init__(self, token: str):
        """

        :param token: Токен авторизации
        """
        pass
    def get_full_info(self) -> dict:
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
