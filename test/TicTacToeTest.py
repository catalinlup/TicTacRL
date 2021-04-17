import unittest
from src.TicTacToe import *

# print("In module products __package__, __name__ ==", __package__, __name__)

class TestTicTacToe(unittest.TestCase):
  def test_x_wins(self):

    expected_board_configuration = "\nXO_\nOX_\n__X\n"
    game = TicTacToe(Board())

    game.make_move(pos(0, 0))
    game.make_move(pos(0, 1))
    game.make_move(pos(1, 1))
    game.make_move(pos(1, 0))
    final_state = game.make_move(pos(2, 2))

    final_board = game.get_board_configuration()

    assert final_state == GameState.WinPlayerX


    assert str(final_board) == expected_board_configuration
  
  def test_o_wins(self):
    expected_board_configuration = "\nXOX\n_OX\n_O_\n"
    game = TicTacToe(Board())

    game.make_move(pos(0, 0))
    game.make_move(pos(0, 1))
    game.make_move(pos(0, 2))
    game.make_move(pos(1, 1))
    game.make_move(pos(1, 2))
    final_state = game.make_move(pos(2, 1))

    final_board = game.get_board_configuration()

    assert final_state == GameState.WinPlayerO
  

    assert str(final_board) == expected_board_configuration

  def test_ends_in_draw(self):
    expected_board_configuration = "\nXOX\nXXO\nOXO\n"

    game = TicTacToe(Board())

    game.make_move(pos(0, 0))
    game.make_move(pos(0, 1))
    game.make_move(pos(1, 0))
    game.make_move(pos(2, 0))
    game.make_move(pos(2, 1))
    game.make_move(pos(2, 2))
    game.make_move(pos(1, 1))
    game.make_move(pos(1, 2))
    final_state = game.make_move(pos(0, 2))

    final_board = game.get_board_configuration()


    assert final_state == GameState.Draw

    assert str(final_board) == expected_board_configuration










