n , k =map(int, input().split())

divisor=[]

for i in range(n):
    if n%(i+1)==0:
        divisor.append(i+1)

if len(divisor) >= k:
    print(divisor[k-1])

else:
    print(0)