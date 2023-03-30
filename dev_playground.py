import escape_visualizer as ev
import numpy as np

board = ev.make_board(side_length = 10)
print(board)

def add_one(coord: tuple[int, int]):
    return (coord[0] + 1, coord[1] + 1)

board = ev.escape_board(func = add_one, board = board,
                        iterations = 1000, escape_thresh = 10**2,
                        side_length = 10, info_requested ='p_num')

print(board)


# coord = ef.decode_coord(board[7, 3], 10)
# print(coord)

# code = board[7, 3]