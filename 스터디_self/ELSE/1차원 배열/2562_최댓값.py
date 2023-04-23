arr=[]
for i in range(9):
    arr.append(int(input()))

print(max(arr))

for i in range(9):
    if max(arr)==arr[i]:
        print(i+1)