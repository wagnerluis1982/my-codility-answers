# https://app.codility.com/demo/results/training35HVFA-Y38/

# Task Score    30%
# Correctness   40%
# Performance   20%

def solution(M: int, A: list) -> int:
    B = set()
    count = 0
    for value in A:
        if value in B:
            count += count_pairs(B)
            B.clear()
        B.add(value)
    count += count_pairs(B)
    return count


def count_pairs(B: set) -> int:
    n = len(B)
    return (n * (n + 1)) // 2
