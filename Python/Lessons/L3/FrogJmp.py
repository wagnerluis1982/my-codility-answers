# https://app.codility.com/demo/results/trainingBWGWPZ-9VA/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(X: int, Y: int, D: int) -> int:
    if X == Y:
        return 0

    jumps, r = divmod(Y - X, D)
    if r > 0:
        jumps += 1

    return jumps
