# https://app.codility.com/demo/results/trainingPQ3AD7-E9Q/

# Task Score    45%
# Correctness   71%
# Performance    0%

def solution(A: list) -> int:
    N = len(A)

    count = 0
    for x in range(N):
        z = x + 2
        for y in range(x + 1, N):
            while (
                z < N
                and A[x] + A[y] > A[z]
                and A[y] + A[z] > A[x]
                and A[z] + A[x] > A[y]
            ):
                z += 1
                count += 1

    return count
