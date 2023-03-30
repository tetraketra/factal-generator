# Imports # -------------------------------------------------------------------
from itertools import cycle
from typing import Callable
import numpy as np



# Public Functions # ----------------------------------------------------------
pass



# Private Functions # ---------------------------------------------------------
def _is_k_periodic(lst: list, k: int) -> bool:
    if len(lst) < k // 2:
        return False

    return np.array(x == y for x, y in zip(lst, cycle(lst[:k]))).all()


def _get_escape_info(func: Callable, coords: tuple[float, float], periods: int, esc_thresh: float) -> tuple[int, int, list]:
    esc_period, periodicity = 0, 0
    history = []
    
    for i in range(periods):
        history.append(coords)
        coords = func(coords)

        if max(coords) >= esc_thresh:
            esc_period = i
            break
    
    if not esc_period:
        for k in range(periods):
            if _is_k_periodic(history, k) and not periodicity: 
                periodicity = k
    
    return esc_period, periodicity, history
    