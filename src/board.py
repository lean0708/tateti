from src.constants import NO_ONE

NEW_LINE_CHARACTER = "\n"
CORNERS_POSITIONS = [1, 3, 7, 9]
CENTER_POSITION = 5


class Board:
    def __init__(self):
        # all positions stay with player 0 (no player) until player 1 or 2 uses it
        self.positions = [NO_ONE for i in range(9)]

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


