# https://app.codility.com/demo/results/trainingMNRMNE-YY5/

# Task Score   100%
# Correctness  100%
# Performance  100%

# Detected time complexity: O(N * log(N)) <~ It should be O(n) 🙁

def solution(A: list) -> int:
    a = b = 1000
    x = y = z = -1000

    for i in range(len(A)):
        if A[i] < a:
            b = a
            a = A[i]
        elif A[i] < b:
            b = A[i]

        if A[i] > z:
            x, y = y, z
            z = A[i]
        elif A[i] > y:
            x = y
            y = A[i]
        elif A[i] > x:
            x = A[i]

    return max(a * b * z, x * y * z)
