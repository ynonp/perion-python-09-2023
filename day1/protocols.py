from typing import Iterable, Sequence, Sized, Protocol, Union


def longer_than(n: int, items: Iterable[Sized]) -> Iterable[Sized]:
    # if len(items) > 5:
    #     print("too long list...")
    return [i for i in items if len(i) > n]


print(longer_than(4, ['a', 'hello', 'really long', 'shrt']))
print(longer_than(4, [[1, 2], [1, 2, 3, 4, 5]]))
print(longer_than(4, filter(lambda n: n == "hello", [
    "a", "b", "hello", "c"
])))



class Bread:
    def price(self):
        return 17.9


class Milk:
    def price(self):
        return 6.9


class HasPrice(Protocol):
    def price(self) -> float:
        pass


def total_price(items: list[HasPrice]) -> float:
    return sum(x.price() for x in items)


print(total_price([Bread(), Bread(), Milk()]))












