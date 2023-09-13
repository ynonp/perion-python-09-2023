import itertools


# def open_ports():
#     port = 1024
#     while True:
#         if is_open(port):
#             yield port
#         port += 1


def five():
    while True:
        yield 5


def two_fives():
    yield 5
    yield 5


def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


for n in itertools.islice(fib(), 10):
    print(n)

print("---")
for n in itertools.takewhile(lambda n: n < 100, fib()):
    print(n)


print(sum(itertools.islice(fib(), 10)))
