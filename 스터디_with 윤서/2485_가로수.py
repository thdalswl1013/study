n = int(input())
streetTrees=[]

def GCD(x, y):
    for i in range(min(x,y), 0, -1):
        if x%i==0 and y%i==0:
            return i
            break

for i in range(n):
    streetTrees.append(int(input()))

gcd = streetTrees[1] - streetTrees[0]
for i in range(2, n):
    gcd = GCD(gcd, streetTrees[i]-streetTrees[i-1])

result = (streetTrees[n-1]-streetTrees[0]) // gcd + 1 - n
print(result)

# 시간 초과
"""
n=int(input())
streetTrees=[]
distance=[]

for i in range(n):
    streetTrees.append(int(input()))
#print(streetTrees) # [1, 3, 7, 13]

for i in range(n-1):
    distance.append(streetTrees[i+1]-streetTrees[i])
#print(distance) # [2, 4, 6]

# 최대공약수
def GCD(x, y):
    for i in range(min(x,y), 0, -1):
        if x%i==0 and y%i==0:
            return i
            break
        
for i in range(1, len(distance)):
    gcd = GCD(distance[0], distance[i])

result=0
for i in distance:
    result+= i//gcd -1

print(result)
"""
