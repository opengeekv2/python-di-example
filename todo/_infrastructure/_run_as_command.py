import sys
from todo.core import left_ports


def run_as_command(todo = left_ports.todo) -> None:
    result = todo()
    if result:
        sys.exit(0)