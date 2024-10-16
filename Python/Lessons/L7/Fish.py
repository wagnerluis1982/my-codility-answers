# https://app.codility.com/demo/results/trainingE8BB8C-G4B/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list, B: list) -> int:
    # A: list
    #   indexes are positions.
    #   values are fish sizes.
    # B: list
    #   0 represents a fish flowing upstream.
    #   1 represents a fish flowing downstream.
    N = len(A)
    fishes = len(A)
    downstream = []
    i = 0
    while i < N:
        if B[i] == 1:
            downstream.append(i)
            i += 1
        elif downstream:
            fishes -= 1
            down_idx = downstream[-1]
            if A[down_idx] < A[i]:
                downstream.pop()
            else:
                i += 1
        else:
            i += 1

    return fishes
