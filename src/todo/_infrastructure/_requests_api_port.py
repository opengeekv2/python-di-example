from typing import Generator
from .._model import ToDo

def get_todos_from_api_with_requests() -> Generator:
    yield ToDo(1, 1, 'hola', False)