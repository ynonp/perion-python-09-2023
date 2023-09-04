from typing import TypedDict, NotRequired, Literal
class Point2D(TypedDict):
    x: int
    y: int
    label: str
    color: NotRequired[Literal['blue', 'red', 'yellow', 'white', 'grey']]

def no_types():
    x = input("what do you like?")
    print(x + 5)

x: Point2D = {'x': 10, 'y': 20, 'label': 'start', 'color': 'white'}

print(x)

