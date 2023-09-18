from typing import Literal
from dataclasses import dataclass
import copy


#
# class Artist:
#     def __enter__(self):
#         print("Entering with blcok”)
#   return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("bye bye")
#
# with Artist() as a:
#     pass



@dataclass
class GridPosition:
    row: int
    column: int


class Grid:
    squares: list[list[str]]
    SIZE = (3, 3)

    def __init__(self):
        self.squares = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def __getitem__(self, index: GridPosition):
        return self.squares[index.row][index.column]

    def __setitem__(self, key: GridPosition, value: Literal['X', 'O', ' ']):
        self.squares[key.row][key.column] = value

    def __iter__(self):
        return GridIterator(index=GridPosition(row=0, column=0), grid=self)

    def play(self, position: GridPosition, player: Literal['X', 'O']):
        if self[position] != ' ':
            raise Exception("Square occupied")
        if player != 'O' and player != 'X':
            raise Exception("Invalid player move")

        self[position] = player


@dataclass
class GridIterator:
    index: GridPosition
    grid: Grid

    def __next__(self):
        value = self.grid[self.index]
        index = self.index

        if self.index.column == 2:
            self.index.column = 0
            self.index.row += 1
        elif self.index.column < 2:
            self.index.column += 1

        if self.index.row > 2 or self.index.column > 2:
            raise StopIteration()

        return index, ' '


class Game:
    def __init__(self, grid: Grid):
        self.grid = grid

    def __enter__(self):
        return copy.deepcopy(self.grid)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def new_game(g: Grid):
    return Game(g)

