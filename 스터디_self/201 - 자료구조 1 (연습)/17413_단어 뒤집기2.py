sentence = input().rstrip()

stack = [] # 스택은 LIFO 출력 방식이라서, 자연스레 뒤집힌 단어가 출력됨
tag = False
res = ''

for i in sentence:
    if i == " ": # 공백이면 stack 비움
        while stack:
            res += stack.pop()
        res += i

    elif i == "<": # 태그 안 단어는 뒤집지 않음
        while stack:
            res += stack.pop()
        tag = True
        res += i

    elif i == ">":
        tag = False
        res += i

    elif tag:
        res += i

    else: # 태그 밖 단어는 뒤집음
        stack.append(i)


# 출력
while stack:
    res += stack.pop()
print(res)