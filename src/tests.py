from src.board import Board
from src.constants import NO_ONE, PLAYER_ONE_LETTER, PLAYER_TWO_LETTER
from src.cpu_player import CPUPlayer


def test_get_winning_move_vertical():
    board = Board()
    board.positions = [
        NO_ONE, PLAYER_ONE_LETTER, PLAYER_TWO_LETTER,
        NO_ONE, PLAYER_ONE_LETTER, PLAYER_TWO_LETTER,
        NO_ONE, NO_ONE, NO_ONE
    ]
    # for player one
    winner_position = board.get_winner_position(PLAYER_ONE_LETTER)
    assert winner_position == 7

    # for player two
    winner_position = board.get_winner_position(PLAYER_TWO_LETTER)
    assert winner_position == 8


def test_get_winning_move_in_diagonal():
    board = Board()
    board.positions = [
        PLAYER_ONE_LETTER, NO_ONE, PLAYER_TWO_LETTER,
        NO_ONE, PLAYER_ONE_LETTER, NO_ONE,
        NO_ONE, NO_ONE, NO_ONE
    ]
    winner_position = board.get_winner_position(PLAYER_ONE_LETTER)
    assert winner_position == 8


def test_get_available_positions():
    board = Board()
    board.positions = [
        NO_ONE, PLAYER_ONE_LETTER, PLAYER_TWO_LETTER,
        NO_ONE, PLAYER_ONE_LETTER, PLAYER_TWO_LETTER,
        NO_ONE, NO_ONE, NO_ONE
    ]
    able_positions = [0, 3, 6, 7, 8]
    assert board.get_available_positions() == able_positions


def test_cpu_smart_winner_move():
    board = Board()
    board.positions = [
        NO_ONE, PLAYER_ONE_LETTER, PLAYER_TWO_LETTER,
        NO_ONE, PLAYER_ONE_LETTER, PLAYER_TWO_LETTER,
        NO_ONE, NO_ONE, NO_ONE
    ]
    cpu_player = CPUPlayer(cpu_letter=PLAYER_TWO_LETTER)
    cpu_move = cpu_player.get_smart_move(board=board, human_letter=PLAYER_ONE_LETTER)
    assert cpu_move == 8


def test_cpu_smart_block_move():
    board = Board()
    board.positions = [
        NO_ONE, PLAYER_ONE_LETTER, PLAYER_TWO_LETTER,
        NO_ONE, PLAYER_ONE_LETTER, NO_ONE,
        NO_ONE, NO_ONE, NO_ONE
    ]
    cpu_player = CPUPlayer(cpu_letter=PLAYER_TWO_LETTER)
    cpu_move = cpu_player.get_smart_move(board=board, human_letter=PLAYER_ONE_LETTER)
    assert cpu_move == 7
