from typing import Callable, Iterable
from .model import ToDo
from todo.core import right_ports


def persist_api_todos_as_csv(
    get_todos_from_api: Callable[[], Iterable[ToDo]] = right_ports.get_todos_from_api,
    persist_todo_as_csv: Callable[[ToDo], bool] = right_ports.persist_todo_as_csv
) -> bool:
    looped = False
    for i, todo in enumerate(get_todos_from_api()):
        if 0 == i:
            looped = True
        if not persist_todo_as_csv(todo):
            return False
    return looped


    

    