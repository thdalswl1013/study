l, p = map(int, input().split())
result= l * p

member=list(map(int, input().split()))

minus=[]

for i in range(5):
    minus.append(member[i] - result)
    print(minus[i], end=' ')