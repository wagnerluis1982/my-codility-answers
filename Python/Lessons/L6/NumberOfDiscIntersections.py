# https://app.codility.com/demo/results/trainingEYSCNB-2KB/

# Source: https://github.com/dudmy/study/blob/master/Codility/NumberOfDiscIntersections.md

# Task Score   100%
# Correctness  100%
# Performance  100%

THRESHOLD = 10_000_000


def solution(A: list) -> int:
    count = 0

    right = []
    left = []
    for i in range(len(A)):
        right.append(i + A[i])
        left.append(i - A[i])
    right.sort()
    left.sort()

    j = 0
    k = 0
    while j < len(A) and k < len(A):
        while k < len(A) and right[j] >= left[k]:
            count += k - j

            if count > THRESHOLD:
                return -1

            k += 1

        j += 1

    return count
