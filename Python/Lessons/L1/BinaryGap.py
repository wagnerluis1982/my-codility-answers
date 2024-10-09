# https://app.codility.com/demo/results/trainingEJGFTF-W62/

# Task Score   100%
# Correctness  100%
# Performance   -

def solution(N: int) -> int:
    gt_gap = 0

    counting = False
    count = 0
    for bit in bin(N)[2:]:
        if bit == '1':
            if count > gt_gap:
                gt_gap = count
            counting = True
            count = 0
        elif counting:
            count += 1

    return gt_gap    
