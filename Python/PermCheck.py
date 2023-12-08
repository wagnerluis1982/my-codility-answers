# https://app.codility.com/demo/results/training85VG4P-PA7/

def solution(A):
    # Implement your solution here
    A.sort()
    N = 1
    for e in A:
        if e != N: 
            return 0
        N += 1
    return 1
