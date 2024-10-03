# https://app.codility.com/demo/results/trainingAD46UU-SNQ/

# Task Score   100%
# Correctness  100%
# Performance  100%

THRESHOLD = 1_000_000_000

def solution(A: list) -> int:
    if len(A) == 1:
        return 0

    inc = 0
    count = 0

    for i in range(0, len(A)):
        if A[i] == 0:
            inc += 1
        elif inc > 0:
            count += inc
            if count > THRESHOLD:
                return -1

    return count
