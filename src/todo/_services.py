from functools import wraps
from inspect import getfullargspec, ismethod, isawaitable
from ._infrastructure.adapters import get_todos_from_api_with_requests, persist_todo_as_csv_with_dict_csv

def _injection(contents):
    def inject(func):
        #@wraps(func)
        def wrapper(*args, **kwargs):
            to_inject = func
            if ismethod(func):
                to_inject = func.__func__
            argspec = getfullargspec(to_inject).args
            if len(argspec) == len(args):
                return func(*args, **kwargs)
            arglist = list(args)
            for arg in argspec:
                parameter_to_inject = contents.get(arg, None)
                if parameter_to_inject:
                    arglist.append(parameter_to_inject)
            if isawaitable(func):
                async def tmp():
                    return (await func(*(arglist), **kwargs))
                return tmp()
            return func(*(arglist), **kwargs)
        return wrapper
    return inject

def _container():
    contents = {
        "get_todos_from_api": get_todos_from_api_with_requests,
        "persist_todo_as_csv": persist_todo_as_csv_with_dict_csv
    }

    return _injection(contents)

inject = _container()
