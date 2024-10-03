# https://app.codility.com/demo/results/trainingAMKBW9-GQU/

# Task Score   62%
# Correctness 100%
# Performance  25%

def solution(A: int, B: int, K: int) -> int:
    for i in range(A, B + 1):
        if i % K == 0:
            A = i
            break
    else:
        return 0

    count = 0
    for i in range(A, B + 1, K):
        count += 1

    return count
