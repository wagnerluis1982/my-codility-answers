# https://app.codility.com/demo/results/training3JENXG-8SQ/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(A: list) -> int:
    return len(set(map(abs, A)))
