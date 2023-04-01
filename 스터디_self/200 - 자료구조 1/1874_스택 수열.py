n= int(input())
num=[]

for i in range(n):
    num.append(int(input())) # 4, 3, 6, 8, 7, 5, 2, 1

cur=1
x=0

stack=[]
answer=[]

for i in range(n):
    while num[i]>=cur:
        stack.append(cur)
        answer.append("+")
        cur+=1

    if stack[-1] == num[i]:
        stack.pop()
        answer.append("-")

    else:
        print("NO")
        x=1
        break

if x==0:
    for i in range(len(answer)):
        print(answer[i])

# print(stack): 1 2 3 4 5 6 7 8