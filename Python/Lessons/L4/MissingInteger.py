# https://app.codility.com/demo/results/trainingRDPEBY-Z9E/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    A.sort()
    seq = 1
    last = 0
    for i in range(len(A)):
        current = A[i]
        if current <= 0:    continue
        if current == last: continue
        if current != seq:  return seq
        last = current
        seq += 1
    return seq
