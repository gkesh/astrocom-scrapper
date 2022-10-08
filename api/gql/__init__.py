from typing import Callable
from logger.workers import error


NAME = "API_GRAPHQL"

def responder(exception: Exception):
    def tolerator(exc: Callable):
        def inner(*args, **kwargs):
            try:
                payload = {
                    "status": True,
                    "data": exc(*args, **kwargs)
                }
            except exception as exp:
                error(NAME, str(exp))
                payload = {
                    "status": False,
                    "error": [str(exp)]
                }
            return payload
        return inner
    return tolerator
