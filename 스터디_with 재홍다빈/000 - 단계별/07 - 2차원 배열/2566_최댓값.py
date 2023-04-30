arr=[]

for i in range(9):
    arr.append(list(map(int, input().split())))

max=-1
x = 0
y = 0

for i in range(9):
    for j in range(9):
        if max<arr[i][j]:
            max=arr[i][j]
            x=i+1
            y=j+1

print(max)
print(x, y)