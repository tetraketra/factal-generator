# Imports # -------------------------------------------------------------------
from typing import Callable, Literal
from itertools import cycle
import numpy as np



# Public Functions # ----------------------------------------------------------
def make_board(side_length: int) -> np.ndarray:
    """
    Generates an encoded square 2d board, such that each point is a reversible code
    representing its coordinates in the associated np.ndarray. `shift_coords()` is
    used to convert this np.ndarray coordinate space to the x,y or x,i coordinate
    space actually wanted for function evaluation.

    Args:
     - `side_length: int`, the side length of the square board.

    Returns:
     - An np.ndarray containing encoded points such that `value = y + x*side_length`

    """
    board = np.zeros((side_length, side_length), np.float64)

    for y, x in np.ndindex(board.shape):
        board[y, x] = y + x*side_length

    return board


def encode_coord(coord: tuple[int, int], side_length: int) -> int: #y,x
    """Converts a 2d point to a single value such that `code = y + x*side_length`"""
    return coord[0] + coord[1]*side_length


def decode_coord(code: int, side_length: int): #y,x
    """Decodes a point code such that `coords = (code%side_length, code//side_length)`"""
    return (code%side_length, code//side_length)


def is_k_periodic(lst: list, k: int) -> bool: #FIXME I think this is wrong, but not sure how?
    """Detects if the list is k-periodic."""
    if len(lst) < k // 2:
        return False
    return np.array(x == y for x, y in zip(lst, cycle(lst[:k]))).all()


def shift_coords(coord: tuple[int, int], real_topleft: tuple[int, int],
                 real_botright: tuple[int, int]) -> tuple[int, int]:
    """Given a coordinate in np.ndarray axes index space, shifts to a hypothetical y,x
    (or i,x if you want to interpret it that way) point used for function evaluation."""
    return coord #TODO


def get_escape_info(func: Callable, code: int, iterations: int,
                    escape_thresh: float, side_length: int,
                    info_requested: Literal["point",
                    "slope", "period"]) -> int:
    """
    Apply a function to a p_num in 2d space until it escapes, then return info.

    Args:
     - `func: Callable`, the function to apply repeatedly.
     - `code: int`, the encoded 2d p_num. See `encode_coord()`.
     - `iterations: int`, the number of times to apply `func`.
     - `escape_thresh: float`, the absolute threshold to be considered escaped.
     - `side_length: int`, the square side-length of the board. Relevant for decoding.
     - `info_requested: Literal[...]`: See return values.

    Returns:
     - If "p_num", the period number at which it escapes (or 0 if doesn't).
     - If "slope", the slope of the final two points before escape (or 0 if it doesn't).
     - If "period", the minimum periodicity of the initial point. CPU: T>T
    """

    coords = decode_coord(code, side_length)
    real_coords = shift_coords(coords, (0,0), (0,0))

    if info_requested == "p_num":
        p_num = 0

        while p_num := p_num + 1:
            real_coords = func(real_coords)

            if max(abs(real_coords[0], real_coords[1])) > escape_thresh:
                return p_num

            if p_num > iterations:
                return 0

    if info_requested == "slope":
        p_num, previous, current = 0, (0,0), real_coords

        while abs(max(current[0], current[1])) <= escape_thresh \
              and (p_num := p_num + 1):

            if p_num > iterations:
                return 0

            previous, current = current, func(real_coords)

        y_change = current[0] / previous[0]
        x_change = current[1] / previous[1]
        return y_change / x_change

    if info_requested == "period":
        raise NotImplementedError # FIXME

# Private Functions # ---------------------------------------------------------
# TODO