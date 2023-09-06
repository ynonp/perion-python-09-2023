from typing import ParamSpec, TypeVar, Callable

P = ParamSpec('P')
T = TypeVar('T')
def logged(f: Callable[P, T]) -> Callable[P, T]:
    def my_version(*args: P.args, **kwargs: P.kwargs):
        print(f"Start: {args}, {kwargs}")
        res = f(*args, **kwargs)
        print(f"End. Result = {res}")
        return res

    return my_version



@logged
def twice(x: int):
    if x == 91:
        return 1
    return x * 2

@logged
def thrice(x: int):
    return x * 3


def one_plus_one(x: int, y: int):
    return x + y

twice('a')
twice(12)
twice(91)
