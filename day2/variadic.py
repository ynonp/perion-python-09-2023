from typing import Iterable, Sized, TypedDict, NotRequired, Optional

def longer_than(n: int, *items: Sized) -> Iterable[Sized]:
    # if len(items) > 5:
    #     print("too long list...")
    return [i for i in items if len(i) > n]



numbers = ['one', 'two', 'three']
print(longer_than(3, "one", "two", "three"))
print(longer_than(3, *numbers))



def sum_words(sentence: str, **weight: int):
    """ returns sum of all words in sentence, according to weight specified """
    return sum(weight.get(word, 0) for word in sentence.split())

# prints 90: 10 + 30 + 50
print(sum_words('I can see the mountains', I=10, can=30, see=50))


class ConnectArgs(TypedDict):
    server: NotRequired[str]
    port: NotRequired[int]
    username: NotRequired[str]
    password: NotRequired[str]

def connect(args: ConnectArgs):
    pass

def connect(
        server: Optional[str] = None,
        port: Optional[int] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
):
    pass


connect(server='123', port=1010)
