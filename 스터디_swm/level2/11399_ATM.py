n=int(input())
person=list(map(int, input().split()))
person.sort()

answer=0
for i in range(1, n+1): # 인출시간이 적은 순으로 정렬하면 됨
    answer+=sum(person[:i])
    
print(answer)
