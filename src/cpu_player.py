from random import randint

from constants import NO_ONE


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
