# https://app.codility.com/demo/results/training8GYEHJ-JUD/

# Task Score    80%
# Correctness   80%
# Performance   80%

# 36 ~> got 26 expected 24

def solution(N: int) -> int:
    min_perimeter = 2 * (1 + N)
    t = 2
    while t ** 2 < N:
        if N % t == 0:
            min_perimeter = min(min_perimeter, 2 * (t + N // t))
        t += 1
    return min_perimeter
