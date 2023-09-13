import urllib.request
from functools import lru_cache
# with urllib.request.urlopen('https://api.ipify.org') as response:
#     data = response.read()
#     print(data)


def after(n: int):
    def decorator(f):
        count = 0

        def inner(*args, **kwargs):
            nonlocal count
            count += 1
            if count <= n:
                return

            return f(*args, **kwargs)

        return inner
    return decorator

def after5(f):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        if count <= 5:
            return

        return f(*args, **kwargs)

    return inner


@after(5)
def doit():
    print("Yo!")

# ignore the first 5 calls
doit()
doit()
doit()
doit()
doit()

# so only print yo once
doit()

def memoize(f):
    memo = {}
    def inner(n: int):
        if n not in memo:
            memo[n] = f(n)

        return memo[n]

    return inner



@lru_cache()
def fib(n):
    print("fib(%d)" % n)
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))


def find_my_ip():
    with urllib.request.urlopen('https://api.ipify.org') as response:
        data = response.read()
        return data.decode('utf8')

def with_ip(f):
    def inner(*args, **kwargs):
        ip = find_my_ip()
        f(ip, *args, **kwargs)

    return inner


@with_ip
def print_first_octet(ip_address: str):
    print(ip_address[0:ip_address.index('.')])


print_first_octet()





