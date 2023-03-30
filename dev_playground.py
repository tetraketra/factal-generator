import escape_visualizer as ev
import numpy as np

board = ev.make_board(side_length = 1000)
print(board)

def add_one_two(coord: tuple[int, int]):
    return (coord[0] + 1, coord[1] + 1)

def loop(coord: tuple[int, int]):
    y, x = coord
    y = y + 1 if y < 5 else y-10
    return (y, x)

board = ev.escape_board(func = loop, board = board,
                        iterations = 20, escape_thresh = 10**2,
                        side_length = 1000, info_requested = 'p_num')

print(board)

# from itertools import islice
# from more_itertools import iterate
# history = list(islice(iterate(loop, (0, 0)), 8))
# print(ev.is_k_periodic(history, 11))

# p = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# a = ev.is_k_periodic(p, 8)
# print(a)
# coord = ef.decode_coord(board[7, 3], 10)
# print(coord)

# code = board[7, 3]