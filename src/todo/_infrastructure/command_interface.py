import sys
from .._use_cases import persist_api_todos_as_csv

def run_as_command() -> None:
    result = persist_api_todos_as_csv()
    if result:
        sys.exit(0)