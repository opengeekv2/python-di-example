from ._infrastructure._requests_api_port import get_todos_from_api_with_requests


def neutral(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def get_todos_from_api(func):
    def wrapper(*args, **kwargs):
        return func(get_todos_from_api_with_requests, *args, **kwargs)
    return wrapper
