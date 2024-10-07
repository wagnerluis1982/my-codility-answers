# https://app.codility.com/demo/results/training8W8V75-GVY/

# Task Score    62%
# Correctness   33%
# Performance   80%

MATCHES = (
    ('(', ')'),
    ('[', ']'),
    ('{', '}'),
)


def solution(S: str) -> int:
    if not S:
        return 1

    stack = []
    for c in S:
        if c in (')', ']', '}'):
            if not stack:
                return 0
            p = stack.pop()
            if (p, c) not in MATCHES:
                return 0
        else:
            stack.append(c)

    return 1
