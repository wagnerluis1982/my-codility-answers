# https://app.codility.com/demo/results/trainingU2WSYZ-W5E/

# Source: https://stackoverflow.com/a/58476097/3707418

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(S, P, Q):
    res = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            res.append(1)
        elif 'C' in S[P[i]:Q[i]+1]:
            res.append(2)
        elif 'G' in S[P[i]:Q[i]+1]:
            res.append(3)
        else:
            res.append(4)
    return res
