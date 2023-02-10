#11047 동전
"""
n, k = map(int, input().split())
coin=[]

for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

count=0

for i in range(n):
    count = count + k//coin[i]
    k = k%coin[i]

print(count)
"""

#1931 강의실 배정
"""
n=int(input())
time=[]

for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])
    
time=sorted(time)
time=sorted(time, key = lambda x:x[1])

last=0
count=0

for i,j in time:
    if i>last:
        count+=1
        last=j

print(count)
"""

# 11399_atm
"""
#SOL1
n=int(input())
people=list(map(int, input().split()))
people.sort()

for i in range(n-1):
    people[i+1]+=people[i]

sum=0
for i in range(n):
    sum+=people[i]
print(sum)
"""

"""
#SOL2
n=int(input())
people=list(map(int, input().split()))
people.sort()

sum=0
for i in range(n):
    sum+=people[i]*(n-i)
print(sum)
"""