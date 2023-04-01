arr=list(input()) # ['2', '1', '4', '3']

for i in range(len(arr)):
    arr[i]=int(arr[i])

arr.sort(reverse=True)

for i in range(len(arr)):
    print(arr[i], end='')