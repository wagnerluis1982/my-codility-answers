# https://app.codility.com/demo/results/trainingMHZD67-7RQ/

# Task Score    22%
# Correctness   40%
# Performance    0%

from collections import defaultdict


def solution(A: list) -> int:
    N = len(A)
    leader, count = leader_and_count(A, 0, N)
    if leader is None:
        return 0

    left = 0
    equileaders = 0
    for s in range(N):
        if A[s] == leader:
            left += 1
            s += 1
            if left > s // 2 and count - left > (N - s) // 2:
                equileaders += 1

    return equileaders


def leader_and_count(A: list, M: int, N: int) -> tuple:
    leader = None
    count = defaultdict(int)

    L = N - M
    for i in range(M, N):
        n = A[i]
        count[n] += 1
        if count[n] > L // 2:
            leader = n
            break

    return leader, count[leader]
