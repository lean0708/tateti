from src.constants import NO_ONE
from src.screen import ask_something

NEW_LINE_CHARACTER = "\n"
WINNER_POSITION_COMBINATIONS = [
    # horizontals
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # verticals
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # diaognals
    [0, 4, 8],
    [2, 4, 6]
]
CENTER_POSITION = 5


class Board:
    def __init__(self):
        # all positions stay with player 0 (no player) until player 1 or 2 uses it
        self.positions = []
        self.reset_board()

    def get_able_positions(self):
        able_positions = []
        for idx, position in enumerate(self.positions):
            if position is NO_ONE:
                able_positions.append(str(idx + 1))
        return able_positions

    def write_a_move(self, player_letter, board_position):
        self.positions[board_position] = player_letter

    def print_board(self):
        string_board = ""
        string_board += """
        [{}][{}][{}]
        [{}][{}][{}]
        [{}][{}][{}]
        """.format(
            self.positions[6], self.positions[7], self.positions[8],
            self.positions[3], self.positions[4], self.positions[5],
            self.positions[0], self.positions[1], self.positions[2],
        )

        return string_board

    def get_winner_letter(self):
        winner_letter = None
        # check for winner
        for winner_combination in WINNER_POSITION_COMBINATIONS:
            # check if all positions are filled with the same letter
            position_one = self.positions[winner_combination[0]]
            position_two = self.positions[winner_combination[1]]
            position_three = self.positions[winner_combination[2]]
            if position_one is not NO_ONE and position_one == position_two and position_two == position_three:
                winner_letter = position_one
                break
        return winner_letter

    def ask_human_next_move(self):
        able_positions = self.get_able_positions()
        human_move_position = ask_something("Wich is your move? (use your numpad as the board): ",
                                            able_positions)
        human_position = int(human_move_position) - 1  # human's "1" is "0" for us
        return human_position

    def reset_board(self):
        self.positions = [NO_ONE for i in range(9)]

    def get_winner_position(self, player_letter):
        winner_move = None
        for winner_combination in WINNER_POSITION_COMBINATIONS:
            if self.positions[winner_combination[0]] == player_letter and \
                    self.positions[winner_combination[1]] == player_letter and \
                    self.positions[winner_combination[2]] is NO_ONE:
                winner_move = winner_combination[2]
                break
            elif self.positions[winner_combination[0]] == player_letter and \
                    self.positions[winner_combination[2]] == player_letter and \
                    self.positions[winner_combination[1]] is NO_ONE:
                winner_move = winner_combination[1]
                break
            elif self.positions[winner_combination[1]] == player_letter and \
                    self.positions[winner_combination[2]] == player_letter and \
                    self.positions[winner_combination[0]] is NO_ONE:
                winner_move = winner_combination[0]
                break
        return winner_move



