#11047 동전
"""
n, k = map(int, input().split())
coin=[]

for i in range(n):
    coin.append(int(input()))    
coin.sort(reverse=True)

result=0
for i in range(n):
    if(k//coin[i] !=0):
        result+=k//coin[i]
        k%=coin[i]
print(result)

"""

#1931 회의실배정
"""
n = int(input())
lecture=[]

for i in range(n):
    start, end = map(int, input().split())
    lecture.append([start, end])

lecture.sort()
lecture.sort(key = lambda x: x[1]) # 끝나는 시간 기준: [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]] 

last=0
result=0

for i, j in lecture:
    if i>=last:
        result+=1
        last=j
print(result)
"""

#11399 ATM
"""
n=int(input())
people= list(map(int, input().split()))
people.sort()

for i in range(n-1):
    people[i+1]+=people[i]

sum=0
for i in range(n):
    sum+=people[i]
print(sum)
"""

#1541 잃어버린 괄호
"""
array=list(input().split('-'))

result=0

for i in array[0].split('+'):
    result+=int(i)

for i in array[1:]:
    for j in i.split('+'):
        result-=int(j)

print(result)
"""

#13305 주유소
n=int(input())

length=list(map(int, input().split())) # 2, 3, 1
weight=list(map(int, input().split())) # 5, 2, 4, 1

result=0
min = weight[0] # 5

for i in range(len(length)):

    if min>weight[i]: # 더 싼 가격이 나오기 전에는 현재 가격으로 충전함
        min=weight[i]

    result += min * length[i] # 제일 처음에는 weight[0] * length[0]
print(result)    

#1459 걷기 


#2012 등수 매기기
"""
n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input())) # 1, 5, 3, 1, 2

arr.sort() # 1, 1, 2, 3, 5

sum=0

for i in range(n):
    sum += abs((i+1) - arr[i]) 

print(sum)
"""