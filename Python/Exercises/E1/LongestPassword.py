# https://app.codility.com/demo/results/trainingCFWXNY-HVG/

# Task Score   100%
# Correctness  100%
# Performance    -

def solution(S: str):
    max_password = -1
    state = ""
    letters = 0
    digits = 0
    for c in S:
        if c.isspace():
            if state == "PW" and letters % 2 == 0 and digits % 2 == 1:
                max_password = max(max_password, letters + digits)
            state = "SP"
            letters = 0
            digits = 0
        elif not c.isalnum():
            state = "BAD"
        elif state != "BAD":
            state = "PW"

        if state == "PW":
            digits += c.isdigit()
            letters += c.isalpha()

    if state == "PW" and letters % 2 == 0 and digits % 2 == 1:
        max_password = max(max_password, letters + digits)

    return max_password
