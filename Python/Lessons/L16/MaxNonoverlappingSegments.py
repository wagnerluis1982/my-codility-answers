# https://app.codility.com/demo/results/trainingZAKHJU-UBD/

# Source: https://codesays.com/2015/solution-to-max-nonoverlapping-segments-by-codility/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list, B: list) -> int:
    N = len(A)
    if N < 2:
        return N

    count = 1
    end = B[0]
    index = 1
    while index < N:
        while index < N and A[index] <= end:
            index += 1
        if index == N:
            break
        count += 1
        end = B[index]

    return count
