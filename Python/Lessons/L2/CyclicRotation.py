# https://app.codility.com/demo/results/training74ZEBW-F49/

# Task Score   100%
# Correctness  100%
# Performance   -

def solution(A: list, K: int) -> list:
    if K == 0:
        return A

    N = len(A)
    R = [0] * N
    for i in range(N):
        R[(i + K) % N] = A[i]

    return R
