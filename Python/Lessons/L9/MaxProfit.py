# https://app.codility.com/demo/results/training6X3EMS-G5E/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    if len(A) < 2:
        return 0

    low = high = A[0]
    profit = 0
    low_idx = high_idx = 0
    for i in range(1, len(A)):
        share = A[i]

        if share > high:
            high = share
            high_idx = i

        if share < low:
            low = share
            low_idx = i

        if low_idx <= high_idx:
            profit = max(profit, high - low)
        else:
            high = low
            high_idx = low_idx

    return profit
