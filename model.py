from config import *
import controller


class Model(dict):
    def __init__(self):
        player_turn = None
        fullmove_number = 1

    def get_xo_at(self, position):
        return self.get(position)

    def get_alphanumeric_position(self, rowcol):
        if self.is_on_board(rowcol):
            row, col = rowcol
            return "{}{}".format(X_AXIS_LABELS[col], Y_AXIS_LABELS[row])

    def is_on_board(self, rowcol):
        row, col = rowcol
        return 0 <= row <= 2 and 0 <=col <=2
