# https://app.codility.com/demo/results/trainingHF7ZF7-6XU/

# Task Score    60%
# Correctness  100%
# Performance   20%

def solution(A: list) -> int:
    table = []

    for i in range(len(A)):
        is_last = i == len(A) - 1
        if not is_last:
            table.insert(i, [A[i]])

        for j in range(i):
            table[j].append(A[i] + table[j][-1])
            table[j][-2] /= (i - j)

            if is_last:
                table[j][-1] /= (i - j + 1)
                table[j] = min(table[j][1:])

    return min(range(len(table)), key=table.__getitem__)
