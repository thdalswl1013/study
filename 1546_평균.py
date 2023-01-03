import math

n=int(input())
list_n=list(map(int, input().split()))
list_new=[]
max_score=max(list_n)

for i in range(n):
    list_new.append(list_n[i]/max_score*100)

sum=0
for i in range(n):
    sum+=list_new[i]
print(sum/n)