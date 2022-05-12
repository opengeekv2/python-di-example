from http.client import HTTPSConnection
from io import BytesIO
import json
from typing import List
from todo.core.model import ToDo


def get_todos_from_api_with_http_client() -> List[ToDo]:
    HOST = 'jsonplaceholder.typicode.com'
    METHOD = 'GET'
    ENDPOINT = '/todos'
    connection = HTTPSConnection(HOST)
    connection.request(METHOD, ENDPOINT)
    response = connection.getresponse()
    return json.load(
        BytesIO(response.read()),
        object_hook=lambda o:
            ToDo(o['userId'], o['id'], o['title'], o['completed'])
    )