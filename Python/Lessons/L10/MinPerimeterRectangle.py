# https://app.codility.com/demo/results/trainingVHTHVV-2BF/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(N: int) -> int:
    min_perimeter = 2 * (1 + N)
    t = 2
    while t ** 2 <= N:
        if N % t == 0:
            min_perimeter = min(min_perimeter, 2 * (t + N // t))
        t += 1
    return min_perimeter
