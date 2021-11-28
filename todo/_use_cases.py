from typing import Callable, Iterable 
from .di import inject
from ._model import ToDo

@inject
def persist_api_todos_as_csv(
    get_todos_from_api: Callable[[], Iterable[ToDo]],
    persist_todo_as_csv: Callable[[ToDo], bool]
) -> bool:
    looped = False
    for i, todo in enumerate(get_todos_from_api()):
        if 0 == i:
            looped = True
        if not persist_todo_as_csv(todo):
            return False
    return looped


    

    