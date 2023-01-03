n=int(input())

divisor=list(map(int, input().split()))
divisor_sorted=sorted(divisor)

if n==1:
    result = divisor_sorted[0]*divisor_sorted[0]
else:
    result= divisor_sorted[0]*divisor_sorted[-1]

print(result)