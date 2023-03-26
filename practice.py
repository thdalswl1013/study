sentence = input()

stack = [] # 스택은 LIFO 출력 방식이라서, 자연스레 뒤집힌 단어가 출력됨
tag = False
res = ''


for i in sentence:
    if i == " ": # 공백이면 stack 비움
        while stack:
            res+=stack.pop()
        res+=i
    
    elif i=="<":
        while stack:
            res+=stack.pop()
        tag=True
        res+=i
    
    elif i==">":
        tag=False
        res+=i

    elif tag:
        res+=i
    
    else:
        stack.append(i)
    
while stack:
    res+=stack.pop()
print(res)