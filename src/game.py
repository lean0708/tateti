from random import randint

from constants import PLAYER_ONE_LETTER, PLAYER_TWO_LETTER
from src.board import Board
from src.cpu_player import CPUPlayer
from src.screen import print_to_screen, ask_something, print_big_message, print_header

NO_ANSWER = 'no'
YES_ANWER = 'yes'


class Game:
    def __init__(self):
        self.human_letter = PLAYER_ONE_LETTER
        self.cpu_letter = PLAYER_TWO_LETTER

    def start(self):
        print_header()
        # board presentation
        board = Board()
        print_to_screen(board.print_board())

        # ask user for a letter
        self.human_letter = ask_something(
            question="Which letter do you prefer? (X/O): ",
            valid_answers=[PLAYER_ONE_LETTER, PLAYER_TWO_LETTER]
        )
        # set cpu letter
        self.cpu_letter = PLAYER_ONE_LETTER if self.human_letter == PLAYER_TWO_LETTER else PLAYER_TWO_LETTER

        cpu_player = CPUPlayer(cpu_letter=self.cpu_letter)

        # randomly assign next player to move
        human_is_the_next = bool(randint(0, 1))

        still_playing = True
        # game begins
        while still_playing:
            while True:
                available_positions = board.get_available_positions()

                if len(available_positions) > 0:

                    if human_is_the_next:
                        # human moves
                        print_to_screen("Your turn:")
                        human_next_move = board.ask_human_next_move(available_positions)
                        board.write_a_move(self.human_letter, human_next_move)
                        human_is_the_next = False
                    else:
                        # CPU player moves
                        print_to_screen("Computer just played:")
                        board.write_a_move(self.cpu_letter, cpu_player.get_smart_move(board, self.human_letter))
                        human_is_the_next = True

                    print_to_screen(board.print_board())
                    winner_letter = board.get_winner_letter()

                    if winner_letter:
                        winner_message = "Computer wins!" if winner_letter == self.cpu_letter else "You win!"
                        print_big_message(message=winner_message)
                        break

                else:
                    print_big_message(message="Game over! It was a draw")
                    break

            play_again = ask_something(
                question="Do you wanna play again? (yes/no): ",
                valid_answers=[YES_ANWER, NO_ANSWER]
            )
            if play_again == YES_ANWER:
                board.reset_board()
                # show empty board again
                print_to_screen(board.print_board())
            else:
                still_playing = False



