import math
n, m = map(int, input().split(':'))

"""
def gcd(x, y):
    for i in range(min(x,y), 0, -1):
        if x%i==0 and y%i==0:
            return i
            break
"""

n_=int(n/math.gcd(n,m))
m_=int(m/math.gcd(n,m))

print('%d:%d' %(n_, m_))