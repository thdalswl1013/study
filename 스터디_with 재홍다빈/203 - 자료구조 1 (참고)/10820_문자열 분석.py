import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    if not line:
        break

    # 소문자, 대문자, 숫자, 공백
    low, up, number, space = 0, 0, 0, 0

    for i in line:
        if i.islower():
            low += 1
        elif i.isupper():
            up += 1
        elif i.isdigit():
            number += 1
        elif i.isspace():
            space += 1

    print(low, up, number, space)