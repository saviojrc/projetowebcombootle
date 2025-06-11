from enum import Enum


class RedirecionamentoEnum(Enum):
    LOGIN = "login"
    LOGIN_COM_FALHA = "login_com_falha"
    SUCESSO_LOGIN = "sucesso_login"
    STYLESHEETS = "static/css"
    JAVASCRIPTS = "static/js"
    IMAGES = "static/img"
    FONTS = "static/fonts"


def get_route_path(rota : RedirecionamentoEnum) -> str:
    """
    Returns the path for a given route name.
    """
    try:
        return rota.value
    except ValueError as e:
        print(f"Error: {e}")
        raise e
