# https://app.codility.com/demo/results/trainingF7KYMR-B6K/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(K: int, A: list) -> int:
    N = len(A)

    ropes = 0
    L = 0
    for i in range(N):
        L += A[i]
        if L >= K:
            ropes += 1
            L = 0

    return ropes
