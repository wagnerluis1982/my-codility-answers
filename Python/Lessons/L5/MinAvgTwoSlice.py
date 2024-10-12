# https://app.codility.com/demo/results/trainingV8H46U-VFN/

# Task Score    50%
# Correctness  100%
# Performance    0%

def solution(A: list) -> int:
    N = len(A)
    P = prefix_sums(A, N)
    V = prefix_averages(P, N)

    index = 0
    lesser = V[0][1]
    x, y = 0, 2
    while y < N:
        if V[x][y] < lesser:
            lesser = V[x][y]
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


def prefix_averages(P: list, N: int) -> list:
    V = [[0] * N for _ in range(N)]
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            V[i][j] = slice(P, i, j)
    return V

def slice(P: list, x: int, y: int) -> float:
    if x > y:
        raise Exception(f"Invalid range: x={x} > y={y}")
    try:
        return (P[y + 1] - P[x]) / (y - x + 1)
    except IndexError:
        raise Exception(f"Invalid index: x={x}, y+1={y + 1}")
