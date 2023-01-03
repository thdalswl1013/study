n, k=map(int,input().split())

arr=[0]*n

for i in range(n):
    arr[i]=i+1 # arr=[1,2,3,4,5,6,7]

answer=[]
num=0

for i in range(n):
    num+=(k-1) #인덱스가 [k-1]인 부분을 제거해야함

    if len(arr) <= num:
        num %=len(arr)

    answer.append(str(arr[num]))
    arr.pop(num)

#print(answer) # ['3', '6', '2', '7', '5', '1', '4'] 출력
print("<", ", ".join(answer), ">", sep = '') # <3, 6, 2, 7, 5, 1, 4> 출력