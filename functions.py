from typing import List

def max_num_pos(array: List[int]):
    max = array[0]
    pos = 0

    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            pos = i

    return {
        "max": max,
        "pos": pos
    }

def primos(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sd(n: int) -> int:
    return sum(int(d) for d in str(n))