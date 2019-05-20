from random import randint

from constants import NO_ONE
from src.board import WINNER_POSITION_COMBINATIONS


class CPUPlayer:
    def __init__(self, cpu_letter):
        self.cpu_letter = cpu_letter

    def get_random_move(self, board_positions_list):
        move_position = None
        steps = 0
        walk_random_steps = randint(1, 9)
        while move_position is None:
            for idx, position in enumerate(board_positions_list):
                if steps >= walk_random_steps and position is NO_ONE:
                    move_position = idx
                    break
                else:
                    steps += 1
        return move_position

    def get_smart_move(self, board, human_letter):
        # first, look for a winner move
        smart_move_position = board.get_winning_position(self.cpu_letter)

        # if there is not a winner move, try to block the human
        if smart_move_position is None:
            smart_move_position = board.get_winning_position(human_letter)

        # if there is not a winner move to block, make a random move
        if smart_move_position is None:
            smart_move_position = self.get_random_move(board.positions)
        return smart_move_position
