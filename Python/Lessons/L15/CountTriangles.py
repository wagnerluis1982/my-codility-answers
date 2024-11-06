# https://app.codility.com/demo/results/trainingAF6SND-S7K/

# Task Score    63%
# Correctness  100%
# Performance    0%

def solution(A: list) -> int:
    N = len(A)
    count = 0

    p = 0
    q = 1
    r = 2
    while p < q < r < N:
        if A[p] + A[q] > A[r] and A[q] + A[r] > A[p] and A[r] + A[p] > A[q]:
            count += 1

        r += 1
        if r == N:
            q += 1
            r = q + 1
            if r == N:
                p += 1
                q = p + 1
                r = p + 2

    return count
