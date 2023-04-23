arr=[0]*31

for i in range(28):
    x=int(input())
    arr[x]=x

for i in range(1, 31):
    if arr[i]==0:
        print(i)