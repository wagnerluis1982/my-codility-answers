# https://app.codility.com/demo/results/trainingHRQ7SW-4AY/

# Task Score    56%
# Correctness  100%
# Performance   12%

THRESHOLD = 10_000_000


def solution(A: list) -> int:
    N = len(A)

    pairs = set()
    intersects = [{p} for p in range(N)]
    for p in range(N):
        for q in range(max(0, p - A[p]), min(N, p + A[p] + 1)):
            if p != q:
                intersects[q].add(p)
                for r in intersects[q]:
                    if p != r:
                        pairs.add((p, r) if p < r else (r, p))
                        if len(pairs) > THRESHOLD:
                            return -1

    return len(pairs)
