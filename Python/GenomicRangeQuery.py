# https://app.codility.com/demo/results/trainingFM4UP8-7VQ/

# Task Score    62%
# Correctness  100%
# Performance    0%

def solution(S: str, P: list, Q: list) -> list:
    factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    def impact(k: int) -> int:
        r = 4
        for i in range(P[k], Q[k] + 1):
            r = min((r, factor[S[i]]))
            if r == 1:
                break
        return r

    return [impact(k) for k in range(min([len(P), len(Q)]))]
