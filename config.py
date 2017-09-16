from configparser import ConfigParser

config = ConfigParser()
config.read('tic_tac_toe_options.ini')

X_COLOR = config.get('tic_tac_toe_colors', 'x_color')
O_COLOR = config.get('tic_tac_toe_colors', 'o_color')
BOARD_COLOR = config.get('tic_tac_toe_colors', 'board_color')

NUMBER_OF_ROWS = 3
NUMBER_OF_COL = 3
DIMENSION_OF_EACH_SQUARE = 124 #124pixels
X_AXIS_LABELS = ('A', 'B', 'C')
Y_AXIS_LABELS = (1, 2, 3)
BOARD_START = {
    'A1':'', 'A2':'', 'A3':'',
    'B1':'', 'B2':'', 'B3':'',
    'C1':'', 'C2':'', 'C3':'',
}
