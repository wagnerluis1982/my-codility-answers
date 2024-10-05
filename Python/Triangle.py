# https://app.codility.com/demo/results/trainingBV468N-H5V/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    if len(A) < 3:
        return 0

    p, q = 0, 1
    for r in range(2, len(A)):
        if (A[p] + A[q] > A[r] and
            A[q] + A[r] > A[p] and
            A[r] + A[p] > A[q]): return 1

        if A[p] < A[r] or A[q] < A[r]:
            if A[p] < A[q]:
                p = r
            else:
                q = r

    return 0
