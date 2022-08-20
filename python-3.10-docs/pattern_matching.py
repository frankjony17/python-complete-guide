# https://peps.python.org/pep-0636/#matching-positional-attributes
from http import HTTPStatus
from x_utils import MimeTypes, process_text, deflate, resend_request, ResourceNotFound, Color


# 1 --------------------------------------------------------------------------------------------------------------------
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 405:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# 2 --------------------------------------------------------------------------------------------------------------------
def handle_reply(reply):
    match reply:
        case (HTTPStatus.OK, MimeTypes.TEXT, body):
            process_text(body)
        case (HTTPStatus.OK, MimeTypes.APPL_ZIP, body):
            text = deflate(body)
            process_text(text)
        case (HTTPStatus.MOVED_PERMANENTLY, new_URI):
            resend_request(new_URI)
        case (HTTPStatus.NOT_FOUND):
            raise ResourceNotFound()


# 3 --------------------------------------------------------------------------------------------------------------------
color = 0

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")


# 4 --------------------------------------------------------------------------------------------------------------------
"""
    Guard:
    We can add an if clause to a pattern, known as a “guard”.
    If the guard is false, match goes on to try the next case block.
    
    Note that value capture happens before the guard is evaluated:
"""


class Point:
    x: int
    y: int


def guard(point):
    match point:
        case Point(x, y) if x == y:
            print(f"The point is located on the diagonal Y=X at {x}.")
        case Point(x, y):
            print(f"Point is not on the diagonal.")
