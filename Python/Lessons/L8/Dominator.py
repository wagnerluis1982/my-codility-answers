# https://app.codility.com/demo/results/trainingMVCZDC-4TS/

# Task Score   100%
# Correctness  100%
# Performance  100%

from collections import defaultdict

def solution(A: list) -> int:
    N = len(A)
    if N == 0 or N == 2:
        return -1
    if N == 1:
        return 0

    index = {}
    count = defaultdict(int)

    for i in range(N):
        value = A[i]
        if value not in index:
            index[value] = i

        count[value] += 1
        if count[value] > N // 2:
            return index[value]

    return -1
