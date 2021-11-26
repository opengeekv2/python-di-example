from typing import List, NamedTuple
from .._model import ToDo
from http.client import HTTPSConnection
import json
from io import BytesIO

def get_todos_from_api_with_requests() -> List[ToDo]:
    connection = HTTPSConnection('jsonplaceholder.typicode.com')
    connection.request('GET', '/todos')
    response = connection.getresponse()
    return json.load(
        BytesIO(response.read()),
        object_hook=lambda o:
            ToDo(o['userId'], o['id'], o['title'], o['completed'])
    )

def persist_todo_as_csv_with_dict_csv(todo: ToDo) -> bool:
    True