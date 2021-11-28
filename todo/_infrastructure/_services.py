from .command_interface import run_as_command
from .adapters import get_todos_from_api_with_http_client, persist_todo_as_csv_with_dict_csv
from .._use_cases import persist_api_todos_as_csv
from todo.di import container

def _feed_container():
    contents = {
        "run": run_as_command,
        "get_todos_from_api": get_todos_from_api_with_http_client,
        "persist_todo_as_csv": persist_todo_as_csv_with_dict_csv,
        "persist_api_todos_as_csv": persist_api_todos_as_csv
    }

    container(contents)

_feed_container()

