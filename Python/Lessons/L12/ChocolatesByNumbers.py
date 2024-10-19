# https://app.codility.com/demo/results/trainingF7VMJ5-7X3/

# Task Score    25%
# Correctness   25%
# Performance   25%

import math


def solution(N: int, M: int) -> int:
    if N == M:
        return 1

    if N < M:
        if M % N == 0:
            return 1
    else:
        if N % M == 0:
            return N // M
        elif N % 2 == 0 and M % 2 == 0:
            return N // (M // 2)

    if M % 2 == 1:
        return N

    return math.gcd(N, M)
