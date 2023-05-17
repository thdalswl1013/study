a, b = map(int,input().split()) # a진법 & b진법
m=int(input())
arr=list(map(int,input().split())) # a진법의 숫자 m개
arr.reverse()


ten = 0
for i in range(m):
    ten += arr[i]*(a**i)

result = []
while ten//b:
    result.append(ten%b)
    ten = ten//b
result.append(ten)

result.reverse()
print(' '.join(map(str,result)))