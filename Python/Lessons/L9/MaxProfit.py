# https://app.codility.com/demo/results/trainingFNUV3Z-2ES/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    if len(A) < 2:
        return 0

    cheapest = A[0]
    profit = 0
    for i in range(1, len(A)):
        cheapest = min(cheapest, A[i])
        profit = max(profit, A[i] - cheapest)

    return profit
