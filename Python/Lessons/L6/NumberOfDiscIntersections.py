# https://app.codility.com/demo/results/trainingJ2TKMW-WYB/

# Task Score    56%
# Correctness  100%
# Performance   12%

THRESHOLD = 10_000_000


def solution(A: list) -> int:
    N = len(A)
    intersects = [set() for _ in range(N)]
    for j in range(N):
        for k in range(max(0, j - A[j]), min(N, j + A[j] + 1)):
            if j != k:
                intersects[k].add(j)

    pairs = set()
    for j, points in enumerate(intersects):
        for k in points:
            pairs.add((j, k) if j < k else (k, j))
            if len(pairs) > THRESHOLD:
                return -1
            for l in points:
                if k != l:
                    pairs.add((k, l) if k < l else (l, k))
                    if len(pairs) > THRESHOLD:
                        return -1

    return len(pairs)
