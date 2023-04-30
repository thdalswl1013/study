arr=[0]*5
for i in range(5):
    arr[i]=int(input())

arr.sort()
print(int(sum(arr)/5))
print(arr[2])
