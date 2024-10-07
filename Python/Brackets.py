# https://app.codility.com/demo/results/trainingXBZNVP-3QX/

# Task Score   100%
# Correctness  100%
# Performance  100%

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

    return 0 if stack else 1
