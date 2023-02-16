n=int(input()) # team 수
people=list(map(int, input().split())) # 역량

people.sort()

result=[]
for i in range(2*n):
    result.append(people[i]+people[2*n -1-i])


print(min(result))