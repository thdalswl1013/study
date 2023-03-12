a, b, L = map(int, input().split())

def GCD(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

def LCM(a, b):
    return (a // GCD(a, b)) * b

def Divisor(n): # 약수 구하기
    for i in range(1, int(n**(0.5)+1)):
        if n % i == 0:
            divisorlst.append(i)
            if i * i != n and i * i <= n:
                divisorlst.append(n//i)


divisorlst = [] # L의 약수 리스트
Divisor(L)
divisorlst.sort()

result= -1
for i in range(len(divisorlst)):
    if LCM(LCM(a, b), divisorlst[i]) == L:
        result = divisorlst[i]
        break

print(result)



# 시간 초과
"""
a, b, L = map(int, input().split())

def GCD(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

def LCM(a, b):
    return (a // GCD(a, b)) * b

def Divisor(n): # 약수 구하기
    for i in range(1, n+1):
        if n % i == 0:
            divisorlst.append(i)



divisorlst = [] # L의 약수 리스트
Divisor(L)
divisorlst.sort()

result= -1
for i in range(len(divisorlst)):
    if LCM(LCM(a, b), divisorlst[i]) == L:
        result = divisorlst[i]
        break

print(result)
"""
