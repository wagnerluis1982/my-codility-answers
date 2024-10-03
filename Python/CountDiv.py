# https://app.codility.com/demo/results/trainingBZB2W8-RUF/

# Task Score   50%
# Correctness 100%
# Performance   0%

def solution(A, B, K):
    return len({i for i in range(A, B + 1) if i % K == 0})
