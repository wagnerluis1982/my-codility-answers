# https://app.codility.com/demo/results/trainingA3C4W9-ZTR/

# Task Score   100%
# Correctness  100%
# Performance  100%

import math

def solution(N: int, M: int) -> int:
    return N // math.gcd(N, M)
