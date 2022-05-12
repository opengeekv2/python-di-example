from todo.core import right_ports
from todo._infrastructure import _get_todos_from_api_with_http_client, _persist_todo_as_csv_with_dict_csv


right_ports.get_todos_from_api = _get_todos_from_api_with_http_client.get_todos_from_api_with_http_client

right_ports.persist_todo_as_csv = _persist_todo_as_csv_with_dict_csv.persist_todo_as_csv_with_dict_csv