def logged(f):
    def my_version(*args, **kwargs):
        print(f"Start: {args}, {kwargs}")
        res = f(*args, **kwargs)
        print(f"End. Result = {res}")
        return res

    return my_version



def twice(x: int) -> int:
    if x == 91:
        return 1
    return x * 2


twice('a')
twice(12)
twice(91)
