# https://app.codility.com/demo/results/training2V594V-THF/

# Task Score    12%
# Correctness   25%
# Performance    0%

# [1, 1, 1] ~> got 1 expected 3

THRESHOLD = 10_000_000

def solution(A: list) -> int:
    N = len(A)

    intersects = set()
    for j in range(0, N - 1):
        if A[j] > 0:
            for k in range(max(0, j - A[j]), min(N, j + A[j])):
                if j == k:
                    continue
                point = (j, k) if j < k else (k, j)
                intersects.add(point)
                if len(intersects) > THRESHOLD:
                    return -1

    return len(intersects)
