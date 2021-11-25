from typing import Callable, Iterable 
from ._services import get_todos_from_api

@get_todos_from_api
def persist_api_todos_as_csv(get_todos_from_api: Callable[[], Iterable]) -> bool:
    try:
        next(iter(get_todos_from_api()))
        return True
    except StopIteration:
        return False

    