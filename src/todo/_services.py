from ._infrastructure.command_interface import run_as_command
from ._infrastructure.adapters import get_todos_from_api_with_http_client, persist_todo_as_csv_with_dict_csv
import todo.inject

def _container():
    contents = {
        "run": run_as_command,
        "get_todos_from_api": get_todos_from_api_with_http_client,
        "persist_todo_as_csv": persist_todo_as_csv_with_dict_csv
    }

    todo.inject._injection(contents)

_container()

