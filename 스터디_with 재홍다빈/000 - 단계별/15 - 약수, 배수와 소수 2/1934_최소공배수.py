t=int(input())

def GCD(a, b): # 최대공약수
    if b==0:
        return a
    else:
        return GCD(b, a%b)
    
for i in range(t):
    a,b=map(int,input().split())

    print(a*b // GCD(a,b))


"""
t=int(input())

def GreatestCommonDivision(a, b): # 최대공약수
    if b==0:
        return a
    else:
        return GreatestCommonDivision(b, a%b)

def LeastCommonMultiple(a, b): # 최소공배수
    return (a*b) // GreatestCommonDivision(a,b)

for i in range(t):
    a,b=map(int, input().split())

    print(LeastCommonMultiple(a,b))

"""

