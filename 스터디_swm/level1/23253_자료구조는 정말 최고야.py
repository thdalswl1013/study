n, m =map(int,input().split()) # 책 4권

p = True
for _ in range(m):
    num = int(input())
    queue = list(map(int, input().split()))

    for j in range(num-1):
        if queue[j] < queue[j+1]:
            p = False
            break

    if not p: 
        break

if p:
    print("Yes")
else:
    print("No")
    

#런타임 에러
"""
n, m =map(int,input().split()) # 책 4권
queue=[0]*m
for i in range(m):
    num=int(input())
    queue[i]=list(map(int, input().split()))
#print(queue) # [[3, 1], [4, 2]]

arr=[]
for i in range(m):
    for j in range(m):
        if queue[i][-1]>queue[j][-1]:
            arr.append(queue[j][-1])
            queue[j].remove(queue[j][-1])
            j+=1
            #print(queue)

        elif queue[i][-1]<=queue[i][-1]:
            arr.append(queue[i][-1])
            queue[j].remove(queue[i][-1])
            i+=1
            #print(queue)
            
if arr==sorted(arr):
    print("Yes")
else:
    print("No")
"""
