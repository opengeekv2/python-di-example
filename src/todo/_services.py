from ._infrastructure.command_interface import run_as_command
from ._infrastructure.adapters import get_todos_from_api_with_http_client, persist_todo_as_csv_with_dict_csv
from todo.di import container

def _feed_container():
    contents = {
        "run": run_as_command,
        "get_todos_from_api": get_todos_from_api_with_http_client,
        "persist_todo_as_csv": persist_todo_as_csv_with_dict_csv
    }

    container(contents)

_feed_container()

