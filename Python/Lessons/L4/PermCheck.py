# https://app.codility.com/demo/results/training85VG4P-PA7/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    A.sort()
    N = 1
    for e in A:
        if e != N: 
            return 0
        N += 1
    return 1
