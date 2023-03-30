import escape_visualizer as ef
import numpy as np

board = ef.make_board(10)
print(board)

coord = ef.decode_coord(board[7, 3], 10)
print(coord)