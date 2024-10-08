# https://app.codility.com/demo/results/trainingPJYE9K-4F2/

# Task Score   100%
# Correctness  100%
# Performance  100%

def solution(H: list) -> int:
    N = len(H)  # width
    if N == 1:
        return 1

    count = 1
    left_height = H[0]
    stack = [left_height]
    for i in range(1, N):
        right_height = H[i]

        # remove height on the left if right height is lesser
        if right_height < left_height:
            while stack and stack[-1] > right_height:
                stack.pop()
            if not stack or stack[-1] < right_height:
                count += 1
                stack.append(right_height)
        # add right height but keep the left one as can still be stacked
        elif right_height > left_height:
            count += 1
            stack.append(right_height)

        left_height = right_height

    return count
