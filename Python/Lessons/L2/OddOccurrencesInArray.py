# https://app.codility.com/demo/results/trainingWG3DGX-BPG/

# Task Score   100%
# Correctness  100%
# Performance  100%

from collections import Counter

def solution(A: list) -> int:
    if len(A) == 1:
        return A[0]

    counter = Counter(A)
    for n, count in counter.items():
        if count % 2 == 1:
            return n

    raise Exception("No unpaired item")
