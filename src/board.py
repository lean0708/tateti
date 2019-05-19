NEW_LINE_CHARACTER = "\n"


class Board:
    def __init__(self):
        # all positions stay with player 0 (no player) until player 1 or 2 uses it
        self.board = [
            [0, 0, 0],  # in this case, i prefer this explicit declaration of the board (for human readable)
            [0, 0, 0],
            [0, 0, 0],
        ]

