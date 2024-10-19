# https://app.codility.com/demo/results/training7VQCVD-NAE/

# Task Score    62%
# Correctness  100%
# Performance   25%

def solution(N: int, M: int) -> int:
    eaten = set()

    x = 0
    while x not in eaten:
        eaten.add(x)
        x = (x + M) % N

    return len(eaten)
