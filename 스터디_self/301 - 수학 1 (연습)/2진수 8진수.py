# 2진수 -> 10진수 -> 8진수
"""
n=(input())
n_list=list(n)


hex_sum=0
for i in range(len(n_list)): # 2진수 -> 10진수
    if n_list[i]=='1':
        hex_sum+=(2**(len(n_list)-1-i))
        
oct_sum=''
while hex_sum != 0: # 10진수 -> 8진수
    oct_sum += str(hex_sum%8)
    hex_sum //= 8
print(oct_sum[::-1])

"""


# 파이썬 내장함수 사용
"""
n=input()
n_=int(n,2)
print(oct(n_)[2:])
"""