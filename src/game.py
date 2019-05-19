from random import randint

from src.board import Board
from src.screen import print_to_screen, ask_something, print_board

PLAYERS_LETTERS = {
    0: " ",  # no player
    1: "X",
    2: "O"
}
NO_PLAYER_LETTER = PLAYERS_LETTERS[0]
PLAYER_ONE_LETTER = PLAYERS_LETTERS[1]
PLAYER_TWO_LETTER = PLAYERS_LETTERS[2]


class Game:
    def __init__(self):
        self.human_letter = PLAYER_ONE_LETTER
        self.cpu_letter = PLAYER_TWO_LETTER

    def start(self):
        # ask user for a letter
        self.human_letter = ask_something(
            question="Wich letter do you prefer? (X/O): ",
            valid_answers=[PLAYER_ONE_LETTER, PLAYER_TWO_LETTER]
        )
        # set cpu letter
        self.cpu_letter = PLAYER_ONE_LETTER if self.human_letter == PLAYER_TWO_LETTER else PLAYER_TWO_LETTER

        board = Board()

        # select first player randomly
        if randint(0, 1):
            print_to_screen("You go first!")
        else:
            print_to_screen("Computer go first!")
            # TODO: hacer un movimiento del cpu antes de empezar el juego

        while True:
            # TODO: pedirle al usuario que haga su jugada
            # TODO: verificar si hay ganador o empate
            print_board(board.board, PLAYERS_LETTERS)
            # TODO: hacer un movimiento del cpu y verificar si hay ganador o empate
            break

