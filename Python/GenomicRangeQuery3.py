# https://app.codility.com/demo/results/trainingJHUPW6-A2X/

# Task Score    62%
# Correctness  100%
# Performance    0%

def solution(S: str, P: list, Q: list) -> list:
    return [calc_impact(S, P, Q, k) for k in range(min((len(P), len(Q))))]


def calc_impact(S: str, P: list, Q: list, k: int) -> int:
    nucleotides = set()
    for i in range(P[k], Q[k] + 1):
        nct = S[i]
        if nct == 'A':
            return 1

        nucleotides.add(nct)
        if len(nucleotides) == 4:
            return 1

    if 'C' in nucleotides:
        return 2
    elif 'G' in nucleotides:
        return 3
    else:
        return 4
