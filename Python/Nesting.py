# https://app.codility.com/demo/results/training72JMT6-6H7/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(S: str) -> int:
    opens = 0
    for c in S:
        if c == '(':
            opens += 1
        else:
            opens -= 1
            if opens < 0:
                return 0

    return int(opens == 0)
