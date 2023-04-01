n=int(input())

arr=[]
for i in range(n):
    arr.append(input().split())

for i in range(n):
    a0=list(arr[i][0])
    a1=list(arr[i][1])
    a0.sort()
    a1.sort()

    if a0==a1:
        print(arr[i][0], "&", arr[i][1], "are anagrams.")
    else:
        print(arr[i][0], "&", arr[i][1], "are NOT anagrams.")

"""
print(arr[0][0][::-1])
print(arr[0][1])
for i in range(n):
    if arr[i][0][::-1] ==arr[i][1]:
        print(arr[i][0], "&", arr[i][1], "are anagrams")
    else:
        print(arr[i][0], "&", arr[i][1], "are NOT anagrams")

"""
