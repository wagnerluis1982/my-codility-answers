# https://app.codility.com/demo/results/trainingCT69D9-GXY/

# Task Score    69%
# Correctness   62%
# Performance   80%

# [-2, 1] ~> got 0 expected 1

def solution(A: list) -> int:
    max_slice = A[0]
    max_ending = max_slice
    for i in range(1, len(A)):
        max_ending = max(0, max_ending + A[i])
        max_slice = max(max_slice, max_ending)
    return max_slice
