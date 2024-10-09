# https://app.codility.com/demo/results/trainingK9PKK5-364/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(X: int, A: list) -> int:
    positions = set(e for e in A if e <= X)

    for P in range(1, X + 1):
        if P not in positions:
            return -1

    for K in range(len(A)):
        positions.discard(A[K])
        if len(positions) == 0:
            return K

    return -1
