# https://app.codility.com/demo/results/training2FXW4J-S58/

# Task Score    87%
# Correctness   75%
# Performance  100%

from math import gcd


def solution(N: int, M: int) -> int:
    if N == M:
        return 1

    if N < M:
        if M % N == 0:
            return 1
        else:
            return N // gcd(N, M)
    else:
        if N % M == 0:
            return N // M
        elif N % 2 == 0 and M % 2 == 0:
            return N // gcd(N, M)

    if M % 2 == 1:
        return N

    return gcd(N, M)
