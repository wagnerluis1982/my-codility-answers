# https://app.codility.com/demo/results/trainingRG8BZE-S63/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(N: int) -> int:
    count = 0

    factor = 1
    while factor ** 2 < N:
        if N % factor == 0:
            count += 2
        factor += 1

    if factor ** 2 == N:
        count += 1

    return count
