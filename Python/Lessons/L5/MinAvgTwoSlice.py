# https://app.codility.com/demo/results/trainingDSE27E-GBF/

# Task Score    60%
# Correctness  100%
# Performance   20%

def solution(A: list) -> int:
    N = len(A)
    P = prefix_sums(A, N)

    index = 0
    lesser = slice(P, 0, 1)
    x, y = 0, 2
    while y < N:
        calc = slice(P, x, y)

        if calc < lesser:
            lesser = calc
            index = x

        y += 1
        if y >= N:
            x, y = x + 1, x + 2

    return index


def prefix_sums(A: list, N: int) -> list:
    P = [0] * (N + 1)
    for k in range(1, N + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def slice(P: list, x: int, y: int) -> float:
    if x > y:
        raise Exception(f"Invalid range: x={x} > y={y}")
    try:
        return (P[y + 1] - P[x]) / (y - x + 1)
    except IndexError:
        raise Exception(f"Invalid index: x={x}, y+1={y + 1}")
