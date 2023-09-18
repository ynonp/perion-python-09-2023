from typing import Literal
from dataclasses import dataclass


@dataclass
class GridPosition:
    row: int
    column: int


class Grid:
    squares: list[list[str]]

    def __init__(self):
        self.squares = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def play(self, position: GridPosition, player: Literal['X', 'O']):
        self.squares[position.row][position.column] = player
