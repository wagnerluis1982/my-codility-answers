# https://app.codility.com/demo/results/trainingCGMRYQ-H24/

# Task Score    30%
# Correctness   40%
# Performance   20%

THRESHOLD = 1_000_000_000


def solution(M: int, A: list) -> int:
    N = len(A)
    B = set()
    count = 0

    p = 0
    q = 0
    while p <= q < N:
        if A[q] in B:
            count += count_pairs(B)
            while p <= q and A[p] != A[q]:
                B.discard(A[p])
                p += 1
            B.discard(A[p])
            count += max(0, q - p - 1)
            if count > THRESHOLD:
                return THRESHOLD
            p = q
            B.clear()
        B.add(A[q])
        q += 1

    count += count_pairs(B)
    return count


def count_pairs(B: set) -> int:
    n = len(B)
    return (n * (n + 1)) // 2
