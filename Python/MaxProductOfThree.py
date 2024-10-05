# https://app.codility.com/demo/results/trainingBVB929-T34/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    if len(A) == 3:
        return A[0] * A[1] * A[2]

    A.sort()
    return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
