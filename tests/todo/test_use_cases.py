from unittest.mock import MagicMock
from todo._use_cases import persist_api_todos_as_csv
from todo._model import ToDo


def test_persist_api_todos_as_csv_is_successful():
    todos = [ToDo(1, 1, 'hola', False)]
    get_todos_from_api = MagicMock(return_value=todos)
    persist_todo_as_csv = MagicMock(return_value=True)
    assert persist_api_todos_as_csv(get_todos_from_api, persist_todo_as_csv)
    assert len(todos) == persist_todo_as_csv.call_count
    
def test_persist_api_todos_as_csv_is_no_successful_no_todos():
    todos = []
    get_todos_from_api = MagicMock(return_value=todos)
    persist_todo_as_csv = MagicMock(return_value=True)
    assert not persist_api_todos_as_csv(get_todos_from_api, persist_todo_as_csv)
    assert len(todos) == persist_todo_as_csv.call_count

def test_persist_api_todos_as_csv_is_no_successful_persist_fails():
    todos = [ToDo(1, 1, 'hola', False)]
    get_todos_from_api = MagicMock(return_value=todos)
    persist_todo_as_csv = MagicMock(return_value=False)
    assert not persist_api_todos_as_csv(get_todos_from_api, persist_todo_as_csv)
    assert len(todos) == persist_todo_as_csv.call_count

