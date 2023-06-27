arr=[]
arr_re=[0]*5

for i in range(5):
    arr.append(int(input()))


for i in range(5):
    if arr[i]<=40:
        arr_re[i]=40
    else:
        arr_re[i]=arr[i]

print(int(sum(arr_re)/5))