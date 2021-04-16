
from enum import Enum
from typing import List, Tuple

class BoardPiece(Enum):
  """
  The state of a TicTacToe cell
  """
  X = 'X',
  O = 'O',
  Empty = 'Empty'

class BoardPosition():
  """
  Describes a position on the Tic Tac Toe Board
  """

  def __init__(self, row: int, column: int) -> None:
    """
    Creates a board position of the provided row and column.
    """
    if row < 0 or row >= 3 or column < 0 or column >= 3:
      raise Exception('Invalid board position ({}, {})'.format(row, column))
    
    self.row = row
    self.column = column

  def get_row(self):
    """
    Return the row corresponding to the provided position
    """
    return self.row

  def get_column(self):
    """
    Return the column corresponding to the provided position
    """
    return self.column

class Board():
  """
  The board of the tic tac toe game
  """

  BOARD_SIZE = 3


  def __init__(self) -> None:
    """
    Ctr. for tic tac toe board
    Creates an initially empty Tic Tac Toe board
    """
    self.board = [[BoardPiece.Empty] * self.BOARD_SIZE] * self.BOARD_SIZE  # the initial state of the board game

  def set_piece(self, position: BoardPosition, piece: BoardPiece) -> None:
    """
    Add the provided board piece to the provided board position
    """
    if piece != BoardPiece.X or piece != BoardPiece.Y:
      raise Exception('Can only place an X piece or an O piece')

    self.board[position.get_row()][position.get_column()] = piece

  def check_cell_piece(self, position: BoardPosition) -> BoardPiece:
    """
    Returns the piece currently at the provided pisition, or BoardPiece.Empty if there is no piece
    """
    return self.board[position.get_row()][position.get_column()]

  def remove_piece(self, position: BoardPosition) -> BoardPiece:
    """
    Removes the piece at the provided position.
    Returns the piece that was originally there, or BoardPiece.Empty,
    if the position was already empty
    """
    original_board_piece = self.check_cell_piece(position)

    self.board[position.get_row()][position.get_column()] = BoardPiece.Empty

    return original_board_piece

  def get_board_size(self):
    return self.BOARD_SIZE

class GameState(Enum):
  WinPlayerX = 'WinPlayerX',
  WinPlayerO = 'WinPlayerO',
  NotOver = 'NotOver'

class GameTurn(Enum):
  PlayerX = 'PlayerX',
  PlayerO = 'PlayerO'

class TicTacToe():
  """
  Class representing an instance of the TicTacToe game.
  """


  def __init__(self, board: Board) -> None:
    """
    Initializes a brand new TicTacToe game instance.

    @param board - the game board object
    """
    self.board = board
    self.game_state = GameState.NotOver
    self.game_turn = GameTurn.PlayerX

  
  def make_move(self, position: BoardPosition) -> GameState:
    """
    Makes a move by placing a piece on the board.
    Based on the current turn places either an X or an O.
    Returns the game state that results in making the move.
    In case the game is over, nothing happens.
    """

    if self.game_state is not GameState.NotOver:
      return self.game_state

    if self.board.check_cell_piece(position) != BoardPiece.Empty:
      raise Exception('Illegal Move! There is already a piece at the specified position')

    piece_to_be_placed = BoardPiece.X if self.game_turn is GameTurn.PlayerX else BoardPiece.O

  def get_board_configuration(self) -> Board:
    """
    Returns the current board configuration
    """
    return self.board

  def get_turn(self) -> GameTurn:
    """
    Returns the current game turn.
    """
    return self.game_turn

  def get_game_state(self) -> GameState:
    """
    Returns the current game state, i.e. whether 
    """
    return self.game_state
    

  def __advance_turn(self) -> None:
    """
    Advances the game turn
    """
    self.game_turn = GameTurn.PlayerX if self.game_turn is GameTurn.PlayerO else GameTurn.PlayerO


  def __compute_game_state_based_on_current_board_confg(self) -> GameState:
    """
    Computes the game states based on the current board configuration.
    Returns the player who won if there are 3 pieces in a row, or GameState.NotOver if nobody has won.
    """
    piece_to_check = BoardPiece.X if self.game_turn is GameTurn.PlayerX else BoardPiece.O
    game_state_to_check = GameState.WinPlayerX if self.game_turn is GameTurn.PlayerX else GameState.WinPlayerO

    if self.__check_piece_for_winning(piece_to_check):
      return game_state_to_check
    
    return GameState.NotOver
  
  def __check_piece_for_winning(self, piece: BoardPiece) -> bool:
    """
    Returns true if the provided piece type is in a winning configuration
    """
    assert piece in [BoardPiece.X, BoardPiece.O] # only X's and O's can form winning configurations


    # check all rows

    for row in range(self.board.get_board_size()):
      if self.__check_row(row, piece):
        return True

    # check all columns

    for col in range(self.board.get_board_size()):
      if self.__check_column(col, piece):
        return True

    
    # check the diagonals
    
    return self.__check_main_diag(piece) or self.__check_second_diag(piece)
    


  def __check_positions(self, positions: List[BoardPosition], for_piece: BoardPiece) -> bool:
    """
    Checl that all cells of the provided board positions contain a piece of the provided type
    """

    for position in positions:
      if self.board.check_cell_piece(position) != for_piece:
        return False

    return True
  
  def __check_row(self, row_num: int, for_piece: BoardPiece) -> bool:
    """
    Check that all cells of the provided row contain the provided board piece
    """
    row_positions = [BoardPosition(row_num, column) for column in range(self.board.get_board_size())]

    return self.__check_positions(row_positions, for_piece)

  def __check_column(self, col_num: int, for_piece: BoardPiece) -> bool:
    """
    Check that all cells of the provided column are of the provided board piece
    """
    col_positions = [BoardPosition(row, col_num) for row in range(self.board.get_board_size())]

    return self.__check_positions(col_positions, for_piece)

  def __check_main_diag(self, for_piece: BoardPiece) -> bool:
    """
    Check that all cells of the main diagonal are of the provided board piece
    """
    main_diag_positions = [BoardPosition(i, i) for i in range(self.board.get_board_size())]

    return self.__check_positions(main_diag_positions, for_piece)

  def __check_second_diag(self, for_piece: BoardPiece) -> bool:
    """
    Check that all cells of the secondary diagonal are of the provided board piece
    """
    second_diag_positions = [BoardPosition(i, self.board.get_board_size() - i) for i in range(self.board.get_board_size())]

    return self.__check_positions(second_diag_positions, for_piece)

