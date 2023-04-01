n, m = map(int, input().split())

"""
m!가 가진 2의개수 - n!이 가진 2의개수 - (m-n)!가 가진 2의개수
                          vs                                    -> 둘 중 작은 수 
m!가 가진 5의개수 - n!이 가진 5의개수 - (m-n)!가 가진 5의개수

"""
def countNum(n, num): # n이 가진 num의 개수를 구하는 함수
    cnt = 0
    divNum = num

    while ( n >= divNum):
        cnt += (n // divNum)
        divNum *= num

    return cnt


print(min(countNum(n, 5)-countNum(m, 5)-countNum(n-m, 5), countNum(n, 2)-countNum(m, 2)-countNum(n-m, 2)))


# 런타임 에러
"""
n, m = map(int,input().split())

def factorial(n):
    if n > 1:
        return factorial(n-1)*n
    elif n == 1:
        return 1

def combination(n,m):
    return factorial(n)/(factorial(m) * factorial(n-m))

result=list(str(int(combination(n,m))))
# print(result)

cnt=0
while (result[-1]=="0"):
    cnt+=1
    result.pop()

print(cnt)

"""
