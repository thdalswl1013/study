arr=[0]*10
for i in range(10):
    arr[i]=int(input())%42

print(len(set(arr))) # "set" 함수