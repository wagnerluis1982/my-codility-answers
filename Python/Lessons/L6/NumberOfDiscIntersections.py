# https://app.codility.com/demo/results/trainingK5SDJ3-SVZ/

# Source: https://github.com/dudmy/study/blob/master/Codility/NumberOfDiscIntersections.md

# Task Score    56%
# Correctness  100%
# Performance   12%

THRESHOLD = 10_000_000


def solution(A: list) -> int:
    count = 0
    for p in range(len(A)):
        J = p + A[p]

        for q in range(p + 1, len(A)):
            K = q - A[q]

            if J >= K:
                count += 1

            if count > THRESHOLD:
                return -1

    return count
