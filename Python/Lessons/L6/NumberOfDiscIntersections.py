# https://app.codility.com/demo/results/trainingS27JHX-AFX/

# Task Score    12%
# Correctness   25%
# Performance    0%

THRESHOLD = 10_000_000

def solution(A: list) -> int:
    N = len(A)
    intersects = set()
    for J in range(N):
        for K in range(max(0, J - A[J]), min(N, J + A[J] + 1)):
            if K != J:
                intersects.add(tuple(sorted([J, K])))
                if len(intersects) > THRESHOLD:
                    return -1

    return len(intersects)
