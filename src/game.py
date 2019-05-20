from random import randint

from constants import PLAYER_ONE_LETTER, PLAYER_TWO_LETTER
from src.board import Board
from src.cpu_player import CPUPlayer
from src.screen import print_to_screen, ask_something


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
        cpu_player = CPUPlayer(cpu_letter=self.cpu_letter)

        # select first player randomly
        if randint(0, 1):
            print_to_screen("You go first!")
        else:
            print_to_screen("Computer go first!")
            board.write_a_move(self.cpu_letter, cpu_player.get_random_move(board.positions))

        while True:
            able_positions = board.get_able_positions()
            if len(able_positions) > 0:
                print_to_screen(board.print_board(), clear_all=False)
                human_move_position = ask_something("Wich is your move? (use your numpad as the board): ",
                                                    able_positions, clear_all=False)
                board.write_a_move(self.human_letter, int(human_move_position) - 1)  # human's "1" is "0" for us
                # TODO: verificar si hay ganador o empate
                board.write_a_move(self.cpu_letter, cpu_player.get_random_move(board.positions))
                print_to_screen("Computer moved:", clear_all=False)

            else:
                print_to_screen("Game over! It was a draw", clear_all=False)
                break

