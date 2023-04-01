n=int(input())

cnt=0

for i in range(n):
    x=input()
    stack=[]

    for i in x:
        if not stack or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()
    
    if not stack:
        cnt+=1
        
print(cnt)
