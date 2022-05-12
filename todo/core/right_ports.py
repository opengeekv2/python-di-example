from typing import Callable, Iterable
from todo.core.model import ToDo


get_todos_from_api: Callable[[], Iterable[ToDo]] = None

persist_todo_as_csv: Callable[[ToDo], bool] = None

run = None
