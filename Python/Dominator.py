# https://app.codility.com/demo/results/training6SB4HF-UA3/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    if not A:
        return -1

    count = {}
    index = {}
    for i in range(len(A)):
        value = A[i]
        if value not in count:
            count[value] = 1
            index[value] = i
        else:
            count[value] += 1

        if count[value] > len(A) // 2:
            return index[value]

    return -1
