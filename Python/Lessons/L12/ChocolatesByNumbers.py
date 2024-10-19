# https://app.codility.com/demo/results/trainingRKQ338-UBX/

# Task Score    62%
# Correctness   50%
# Performance   75%

# [12, 21] ~> got 12 expected 4

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
            return N // math.gcd(N, M)

    if M % 2 == 1:
        return N

    return math.gcd(N, M)
