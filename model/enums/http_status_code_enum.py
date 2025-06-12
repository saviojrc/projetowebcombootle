from enum import Enum
from http import HTTPStatus


class HTTPStatusCodeEnum(Enum):
    """
    Enum for HTTP status codes.
    """

    OK = HTTPStatus.OK.value
    CREATED = HTTPStatus.CREATED.value
    ACCEPTED = HTTPStatus.ACCEPTED.value
    NO_CONTENT = HTTPStatus.NO_CONTENT.value
    BAD_REQUEST = HTTPStatus.BAD_REQUEST.value
    UNAUTHORIZED = HTTPStatus.UNAUTHORIZED.value
    FORBIDDEN = HTTPStatus.FORBIDDEN.value
    NOT_FOUND = HTTPStatus.NOT_FOUND.value
    METHOD_NOT_ALLOWED = HTTPStatus.METHOD_NOT_ALLOWED.value
    CONFLICT = HTTPStatus.CONFLICT.value
    INTERNAL_SERVER_ERROR = HTTPStatus.INTERNAL_SERVER_ERROR.value
    SERVICE_UNAVAILABLE = HTTPStatus.SERVICE_UNAVAILABLE.value


def get_http_status_code(status: HTTPStatusCodeEnum) -> int:
    """
    Returns the integer value of a given HTTP status code.
    """
    try:
        return status.value
    except ValueError as e:
        print(f"Error: {e}")
        raise e
