# https://app.codility.com/demo/results/trainingW899FY-P4V/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    N = len(A)
    if N == 2:
        return abs(A[0] - A[1])

    L = 0
    R = sum(A)
    min_diff = None
    for i in range(N - 1):
        L += A[i]
        R -= A[i]
        cur_diff = abs(L - R)
        if min_diff is None or cur_diff < min_diff:
            min_diff = cur_diff

    return min_diff
