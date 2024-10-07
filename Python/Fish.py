# https://app.codility.com/demo/results/trainingT8222F-QNQ/

# Task Score    37%
# Correctness   50%
# Performance   25%

def solution(A: list, B: list) -> int:
    # A: list
    #   indexes are positions.
    #   values are fish sizes.
    # B: list
    #   0 represents a fish flowing upstream.
    #   1 represents a fish flowing downstream.
    fishes = len(A)
    downstream = []
    for i in range(len(A)):
        if B[i] == 1:
            downstream.append(i)
        elif B[i] == 0 and downstream:
            fishes -= 1
            down_idx = downstream[-1]
            if A[down_idx] < A[i]:
                downstream.pop()

    return fishes
