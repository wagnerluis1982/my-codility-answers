# https://app.codility.com/demo/results/trainingD249XU-85E/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    max_slice = max_ending
    max_ending = A[0]
    for i in range(1, len(A)):
        max_ending = max(A[i], max_ending + A[i])
        max_slice = max(max_slice, max_ending)
    return max_slice
