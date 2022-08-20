from enum import Enum


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


class MimeTypes(Enum):
    TEXT = "TEXT"
    APPL_ZIP = "ZIP"


body = {}


def process_text(_):
    pass


def deflate(_):
    pass


def resend_request(_):
    pass


class ResourceNotFound(Exception):
    def __init__(self):
        pass


class ContextManager:
    pass


context = ContextManager()


expression = 1 * 2
