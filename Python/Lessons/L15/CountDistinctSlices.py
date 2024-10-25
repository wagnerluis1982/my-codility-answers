# https://app.codility.com/demo/results/trainingW6DHBV-JUR/

# Source: https://github.com/Mickey0521/Codility-Python/blob/master/CountDistinctSlices_high_performance.py

# Task Score   100%
# Correctness  100%
# Performance  100%

THRESHOLD = 1_000_000_000


def solution(M: int, A: list) -> int:
    N = len(A)
    B = set()
    count = 0

    p = 0
    q = 0
    while p <= q < N:
        if A[q] not in B:
            count += q - p + 1
            if count > THRESHOLD:
                return THRESHOLD
            B.add(A[q])
            q += 1
        else:
            B.remove(A[p])
            p += 1

    return count
