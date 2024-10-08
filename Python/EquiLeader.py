# https://app.codility.com/demo/results/training2VRAYE-9PC/

# Task Score    11%
# Correctness   20%
# Performance    0%

from collections import defaultdict


def solution(A: list) -> int:
    N = len(A)
    leader = find_leader(A, 0, N)
    if leader is None:
        return 0

    count = 0
    equileaders = 0
    for s in range(N):
        if A[s] == leader:
            count += 1
            S = s + 1
            if count > S // 2 and N - S >= N // 2 and leader == find_leader(A, S, N):
                equileaders += 1

    return equileaders


def find_leader(A: list, M: int, N: int) -> int:
    leader = None

    L = N - M
    if L == 1:
        return A[0]
    elif L != 2:
        count = defaultdict(int)
        for i in range(M, N):
            n = A[i]
            count[n] += 1
            if count[n] > L // 2:
                leader = n
                break

    return leader
