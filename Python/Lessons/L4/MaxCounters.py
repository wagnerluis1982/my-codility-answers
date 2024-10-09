# https://app.codility.com/demo/results/trainingMN4F3W-YF3/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(N: int, A: list) -> list:
    max_applied = 0
    max_counter = 0
    counters = [0] * N

    for K in range(len(A)):
        X = A[K] - 1
        if X < N:
            counters[X] = max(counters[X], max_applied) + 1
            max_counter = max(counters[X], max_counter)
        else:
            max_applied = max_counter

    for X in range(N):
        counters[X] = max(counters[X], max_applied)

    return counters
