from typing import Generator
from todo._model import ToDo
from todo._infrastructure._requests_api_port import get_todos_from_api_with_requests

def test_returns_a_generator():
    result = get_todos_from_api_with_requests()
    assert isinstance(result, Generator)
    assert isinstance(next(result), ToDo)
