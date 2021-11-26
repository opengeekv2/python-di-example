from typing import List
from todo._model import ToDo
from todo._infrastructure.adapters import get_todos_from_api_with_http_client, persist_todo_as_csv_with_dict_csv
import csv
from datetime import date
from os import remove

def test_get_todos_from_api_with_http_client_returns_a_list_with_todo():
    result = get_todos_from_api_with_http_client()
    assert isinstance(result, List)
    assert isinstance(next(iter(result)), ToDo)

def test_persist_todo_as_csv_with_dict_csv_writes_file():
    todo = ToDo(1, 1, 'hola', False)
    today = date.today()
    assert persist_todo_as_csv_with_dict_csv(todo)
    filename_params = (today.year, today.month, today.day, todo.id)
    filename = './storage/{}_{}_{}_{}.csv'.format(*filename_params)
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            assert int(row['userId']) == todo.userId
            assert int(row['id']) == todo.id
            assert row['title'] == todo.title
            assert ('True' == row['completed']) == todo.completed
    remove(filename)




