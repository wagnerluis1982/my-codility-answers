# https://app.codility.com/demo/results/trainingNQCEVQ-RPB/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: int, B: int, K: int) -> int:
    # first number divisible
    for i in range(A, B + 1):
        if i % K == 0:
            A = i
            break
    else:
        return 0

    # last number divisible
    for i in reversed(range(A, B + 1)):
        if i % K == 0:
            B = i
            break

    # shift numbers to get result out of a perfect division
    A, B = K, B - (A - K)

    return B // A
