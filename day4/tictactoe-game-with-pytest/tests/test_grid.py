import tictactoe.grid as grid
# 3. Change interface (and tests) so we'll be able to write:

# for index, square in grid:
#     pass
#
# assert g[index] == 'X'

def test_board_starts_empty():
    g = grid.Grid()

    # for index, square in grid:
    #     pass

    for i in range(3):
        for j in range(3):
            assert g.squares[i][j] == ' '


def test_play_changes_square_value():
    g = grid.Grid()
    index = grid.GridPosition(row=0, column=1)
    g.play(index, 'X')
    assert g.squares[0][1] == 'X'


# 1. Implement Functionality so that this works:
def test_play_on_occupied_square_does_nothing():
    g = grid.Grid()
    index = grid.GridPosition(row=0, column=1)
    g.play(index, 'X')
    g.play(index, 'O')

    assert g.squares[0][1] == 'X'

# 2. Add Tests
# - play outside the board fails
# - play with invalid player character play(GridPosition(row=1, column=1), 'A')

# with pytest.raises(ValueError):
#     g.play(grid.GridPosition(0, 0), 'O')


