n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

cnt=n

#print(cnt)
for i in range(n):
    origin=arr[i]
    error=0   

    for j in range(len(origin)-1):
        if origin[j] == origin[j+1]:
            pass

        elif origin[j] in origin[j+1:]:
            cnt -= 1
            break

print(cnt)