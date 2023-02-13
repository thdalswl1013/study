a, b = map(int, input().split())

a_prime = a//100 + (a%100)//10 * 10 + a%10 * 100
b_prime = b//100 + (b%100)//10 * 10 + b%10 * 100

print(max(a_prime, b_prime))


#another solution1
"""
a, b = map(int, input().split())

def reverse(x):
    return x//100 + (x%100)//10 * 10 + x%10 * 100

print(max(reverse(a), reverse(b)))
"""


#another solution2
"""
a, b = input().split()

a = a[::-1] # 문자열을 뒤집어주는 역할
b = b[::-1]

print(max(a, b))
"""
