# https://app.codility.com/demo/results/training7QCDAZ-RAB/

# Task Score    50%
# Correctness   60%
# Performance   40%

def solution(A: list) -> int:
    N = len(A)
    P = prefix_sums(A, N)

    index = 0
    x, y = 0, 1
    lesser = slice(P, x, y)
    while y < N:
        calc = slice(P, x, y)
        if calc <= lesser:
            lesser = calc
            index = x
            y += 1
        else:
            x, y = x + 1, x + 2

    return index


def prefix_sums(A: list, N: int) -> list:
    P = [0] * (N + 1)
    for k in range(1, N + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def slice(P: list, x: int, y: int) -> int:
    if x > y:
        raise Exception(f"Invalid range: x={x} > y={y}")
    try:
        return P[y + 1] - P[x]
    except IndexError:
        raise Exception(f"Invalid index: x={x}, y+1={y + 1}")
