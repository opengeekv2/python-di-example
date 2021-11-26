from typing import List
from todo._model import ToDo
from todo._infrastructure.adapters import get_todos_from_api_with_requests

def test_returns_a_list():
    result = get_todos_from_api_with_requests()
    assert isinstance(result, List)
    assert isinstance(next(iter(result)), ToDo)
