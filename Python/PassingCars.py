# https://app.codility.com/demo/results/training8DJ5HX-UWE/

# Task Score    90%
# Correctness   80%
# Performance  100%

THRESHOLD = 1_000_000_000

def solution(A: list) -> int:
    # Implement your solution here
    if len(A) == 1:
        return 0

    count = 0
    inc = 1
    start = A[0]

    for i in range(1, len(A)):
        if A[i] == start:
            inc += 1
        else:
            count += inc
            if count > THRESHOLD:
                return -1

    return count
