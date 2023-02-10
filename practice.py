#11047_동전
"""
n, k= map(int, input().split())
coin=[]

for i in range(n):
    coin.append(int(input())) 
coin.sort(reverse=True) # 역순 정렬: 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1

count=0
for i in range(n):
    if k==0:
        break

    else:
        count += k//coin[i] # 큰 숫자부터 집어넣어보기 
        k %= coin[i]
        
print(count)
"""

# 1931_강의실 배정
"""
n = int(input())
time=[]

for i in range(n):
    start, end = map(int, input().split())
    time.append([start,end])

time=sorted(time)
time = sorted(time, key=lambda a: a[1]) 
print(time) # 회의가 빨리 "끝나는" 순으로 정렬


last = 0 # 마지막 회의 시간
cnt = 0 # 회의 개수

for i, j in time: # [i, j]
  if i >= last: # 회의 시작 시간 >= 마지막 회의 시간 
    cnt += 1
    last = j

print(cnt)

"""

# 11499_atm

n=int(input())

people=list(map(int, input().split())) # 3 1 4 3 2
people.sort() # 1 2 3 3 4

for i in range(1, n):
    people[i]+=people[i-1] # 1 3 6 9 13

sum=0
for i in range(n):
    sum+=people[i]

print(sum)