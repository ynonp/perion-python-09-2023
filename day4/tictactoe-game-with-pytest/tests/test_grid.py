import tictactoe.grid as grid
import pytest
# 3. Change interface (and tests) so we'll be able to write:

# for index, square in grid:
#     pass
#
# assert g[index] == 'X'


def test_board_starts_empty():
    g = grid.Grid()

    for index, square in g:
        assert square == ' '


def test_play_changes_square_value():
    g = grid.Grid()
    index = grid.GridPosition(row=0, column=1)
    g.play(index, 'X')
    assert g[index] == 'X'


# 2. Add Tests
# - play outside the board fails
# - play with invalid player character play(GridPosition(row=1, column=1), 'A')

def test_play_outside_board():
    g = grid.Grid()
    with pytest.raises(Exception):
        index = grid.GridPosition(row=9, column=1)
        g.play(index, 'X')

def test_play_invalid_player():
    g = grid.Grid()
    with pytest.raises(Exception):
        index = grid.GridPosition(row=0, column=1)
        g.play(index, 'A')

def test_play_occupied_square():
    g = grid.Grid()
    with pytest.raises(Exception):
        index = grid.GridPosition(row=0, column=1)
        g.play(index, 'X')
        g.play(index, 'O')


def test_play_only_changes_one_square():
    g = grid.Grid()
    index = grid.GridPosition(row=0, column=0)
    g.play(index, 'X')
    for i, val in g:
        if i == index:
            continue
        assert g[i] == ' '


def test_with_game():
    g = grid.Grid()
    with grid.new_game(g) as game:
      game.play(grid.GridPosition(row=0, column=0), 'X')

    assert empty(g)

    with grid.new_game(g) as game:
      game.play(grid.GridPosition(row=0, column=0), 'X')
      game.play(grid.GridPosition(row=0, column=1), 'O')

    assert empty(g)


def empty(g: grid.Grid):
    for index, square in g:
        if square != ' ':
            return False

    return True
