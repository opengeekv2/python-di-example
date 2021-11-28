import sys
from ..di import inject 

@inject
def run_as_command(persist_api_todos_as_csv) -> None:
    result = persist_api_todos_as_csv()
    if result:
        sys.exit(0)