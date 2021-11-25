from unittest.mock import patch
import todo._services

@patch('todo._services.get_todos_from_api', todo._services.neutral)
def test_persist_api_todos_as_csv_is_successful():
    from todo._use_cases import persist_api_todos_as_csv
    def not_empty():
        return ['a']
    assert persist_api_todos_as_csv(not_empty)

@patch('todo._services.get_todos_from_api', todo._services.neutral)
def test_persist_api_todos_as_csv_is_not_successful():
    from todo._use_cases import persist_api_todos_as_csv
    def empty():
        return []
    assert not persist_api_todos_as_csv(empty)
