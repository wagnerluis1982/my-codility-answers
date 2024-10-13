# https://app.codility.com/demo/results/trainingYEJ9AW-YKZ/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    N = len(A)

    S = [0] * (N + 1)
    for k in range(1, N + 1):
        S[k] = S[k - 1] + A[k - 1]

    index = 0
    lowest = slice(S, 0, 1)
    for p in range(N - 1):
        for q in (p + 1, min(p + 2, N - 1)):
            avg = slice(S, p, q)
            if avg < lowest:
                lowest = avg
                index = p

    return index


def slice(S: list, x: int, y: int) -> float:
    return (S[y + 1] - S[x]) / (y - x + 1)
