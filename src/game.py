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
            question="Wich letter do you prefer? (X/O): ",
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
                able_positions = board.get_able_positions()

                if len(able_positions) > 0:

                    if human_is_the_next:
                        # human moves
                        print_to_screen("You move:")
                        human_next_move = board.ask_human_next_move()
                        board.write_a_move(self.human_letter, human_next_move)
                        human_is_the_next = False
                    else:
                        # CPU player moves
                        print_to_screen("Computer moves:")
                        board.write_a_move(self.cpu_letter, cpu_player.get_random_move(board.positions))
                        human_is_the_next = True

                    print_to_screen(board.print_board())
                    winner_letter = board.get_winner_letter()

                    if winner_letter:
                        winner_name = "Computer" if winner_letter == self.cpu_letter else "You"
                        print_big_message(message="Winner is {}!".format(winner_name))
                        break

                else:
                    print_big_message(message="Game over! It was a draw")
                    break

            play_again = ask_something(
                question="Do you wanna play again? (yes/no)",
                valid_answers=[YES_ANWER, NO_ANSWER]
            )
            if play_again == YES_ANWER:
                board.reset_board()
                # show empty board again
                print_to_screen(board.print_board())
                # revert innitial player
                human_is_the_next = not human_is_the_next
            else:
                still_playing = False



