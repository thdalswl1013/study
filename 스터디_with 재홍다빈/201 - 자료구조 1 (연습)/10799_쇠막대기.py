# 이해가 어려움

x = list(input())
answer = 0
stack = []

for i in range(len(x)):
    if x[i] == '(':
        stack.append('(')

    else:
        if x[i-1] == '(': # ')'가 나오고 이전 문자가 '('
            stack.pop()
            answer += len(stack) # 현재 stack에 쌓인 '('개수(=쇠막대기 개수)만큼 개수를 더해준다.

        elif x[i-1] == ')': # ')'가 나오고 이전 문자도 ')'
            stack.pop() 
            answer += 1

print(answer)