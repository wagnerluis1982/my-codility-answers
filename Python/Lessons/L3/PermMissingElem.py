# https://app.codility.com/demo/results/training63HGVJ-Y8M/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    if not A:
        return 1

    A.sort()
    seq = 1
    for n in A:
        if n != seq:
            return seq
        seq += 1

    return seq
