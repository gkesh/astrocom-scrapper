from typing import Callable


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
                payload = {
                    "status": False,
                    "error": [str(exp)]
                }
            return payload
        return inner
    return tolerator
