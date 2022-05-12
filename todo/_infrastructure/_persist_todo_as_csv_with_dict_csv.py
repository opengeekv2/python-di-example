from csv import DictWriter
from datetime import date
from typing import List
from todo.core.model import ToDo


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