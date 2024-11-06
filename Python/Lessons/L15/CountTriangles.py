# https://app.codility.com/demo/results/trainingJC6K4R-F5K/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    N = len(A)
    A.sort()

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
            count += z - y - 1

    return count
