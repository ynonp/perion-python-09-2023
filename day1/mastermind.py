import re
from dataclasses import dataclass
from typing import Sequence

colors = {
    1: 'Red',
    2: 'Green',
    3: 'Blue',
    4: 'Yellow',
    5: 'Brown',
    6: 'Orange',
    7: 'Black',
    8: 'White'
}


def create_all_values_in_range(n: int=4) -> list[int]:
    def valid(n: int):
        s = str(n)
        if re.search(r'[09]', s):
            return False
        if re.search(r'(\d).*\1', s):
            return False
        return True

    return list(filter(valid, range(10 ** (n-1), 10 ** n)))


def digits(n: int) -> Sequence[int]:
    return [int(d) for d in str(n)]


def print_number(n: int):
    for d in digits(n):
        print(colors[d], end=',')
    print('')


@dataclass
class Result:
    red: int
    white: int


def compare(n1: int, n2: int):
    white = 0
    red = 0

    for index1, digit1 in enumerate(digits(n1)):
        for index2, digit2 in enumerate(digits(n2)):
            if digit1 == digit2:
                if index1 == index2:
                    red += 1
                else:
                    white += 1

    return Result(red=red, white=white)


def process_result(*, all_options: list[int], guessed: int, result: Result) -> Sequence[int]:
    return list(filter(lambda opt: compare(opt, guessed) == result, all_options))


class Game:
    def __init__(self):
        self.all_options = create_all_values_in_range()
        self.last_result = Result(0, 0)
        self.next_guess = 1234

    def set_result(self, result: Result) -> None:
        self.last_result = result
        self.all_options = process_result(
            all_options=self.all_options,
            guessed=self.next_guess,
            result=result)
        self.next_guess = self.all_options[0]
