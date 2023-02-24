n=int(input())
thing=[]
for i in range(n):
    thing.append(float(input()))

for i in range(n):
    thing[i]*=0.8

for i in range(n):
    print('$%0.2f' %thing[i])