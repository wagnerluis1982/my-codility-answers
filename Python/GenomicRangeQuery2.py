# https://app.codility.com/demo/results/training4V5JQD-WRY/

# Task Score    62%
# Correctness  100%
# Performance    0%

def solution(S: str, P: list, Q: list) -> list:
    factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    def calcImpact(k: int) -> int:
        impacts = set()
        for i in range(P[k], Q[k] + 1):
            n = factor[S[i]]
            if n == 1:
                return 1

            impacts.add(n)
            if len(impacts) == 4:
                return 1

        return min(impacts)

    return [calcImpact(k) for k in range(min([len(P), len(Q)]))]
