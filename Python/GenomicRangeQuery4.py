# https://app.codility.com/demo/results/trainingSX237A-2CJ/

# Task Score    62%
# Correctness  100%
# Performance    0%

def solution(S: str, P: list, Q: list) -> list:
    T = [impact(s) for s in S]
    return [min(T[P[k]:Q[k]+1]) for k in range(min((len(P), len(Q))))]


def impact(s: str) -> int:
    if s == 'A':
        return 1
    elif s == 'C':
        return 2
    elif s == 'G':
        return 3
    else:
        return 4
