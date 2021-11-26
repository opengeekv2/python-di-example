from typing import List
from .._model import ToDo
from http.client import HTTPSConnection
import json
from io import BytesIO
from datetime import date
from csv import DictWriter


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

def persist_todo_as_csv_with_dict_csv(todo: ToDo) -> bool:
    today = date.today()
    filename = './storage/{}_{}_{}_{}.csv'.format(
        today.year,
        today.month,
        today.day,
        todo.id
    )
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as fd:
            todo_dict = todo.__dict__
            dw = DictWriter(fd, fieldnames=todo_dict.keys())
            dw.writeheader()
            dw.writerow(todo_dict)
        return True
    except BaseException as ex:
        print(ex)
        return False
