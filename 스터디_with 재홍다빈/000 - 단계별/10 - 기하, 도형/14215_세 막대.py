a,b,c=map(int,input().split())

arr=[0]*3
arr[0]=a;arr[1]=b;arr[2]=c
arr.sort()

if arr[0]+arr[1]==arr[2]:
    print(sum(arr)-1)

elif arr[0]+arr[1]<arr[2]:
    print(sum(arr)-(arr[2]-(arr[0]+arr[1])+1))

else:
    print(sum(arr))