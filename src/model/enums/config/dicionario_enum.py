from enum import Enum

from src.util.file_util import FileUtil


class DicionariosEnum(Enum):
    """
     Dicionários de configuração do sistema.
    - DB_SERVICE: Configurações do serviço de banco de dados.
    - WEB_SERVICE: Configurações do serviço web.
    - CONFIG_REMOTE: Configurações de acesso remoto.
    """

    DB_SERVICE = (
        FileUtil
        .get_payload()
        .get('data')
        .get('services')
        .get('db_service'))

    WEB_SERVICE = (
        FileUtil
        .get_payload()
        .get('data')
        .get('services')
        .get('web_server'))

    CONFIG_REMOTE = (
        FileUtil
        .get_payload()
        .get('data')
        .get('services')
        .get('config_remote'))


def obter_dicionario(dicionario: DicionariosEnum):
    """
    Obtém o dicionário de configuração especificado.
    :param dicionario: Enumeração do dicionário a ser obtido.
    :return: Dicionário de configuração.
    """
    return dicionario.value
