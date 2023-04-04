""" 
ex) n=4라 하자
    1 = (1)
    2 = (1 + 1), (2)
    3 = (1 + 1 + 1), (1 + 2), (2 + 1), (3)
    4 = (1 + 1 + 1 + 1), (1 + 1 + 2), (1 + 2 + 1), (1 + 3), (2 + 1 + 1), (2 + 2), (3 + 1)
            
    4에는 1에 위의 3에서 더해졌던 숫자들이 더해지고, 
          2에 위의 2에서 더해졌던 숫자들이 더해지고,
          3에 위의 1에서 더해졌던 숫자들이 더해진다.
"""

# DFS
"""
def sol(n):
    if n==1:
        return 1 # 1
    elif n==2:
        return 2 # 1+1, 2
    elif n==3:
        return 4 # 1+2, 2+1, 3, 1+1+1
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)

n=int(input())

for i in range(n):
    a = int(input())
    print(sol(a))
"""


n=int(input())

for i in range(n):
    a = int(input())

    dp=[0]*(a+1)
    # print(dp)

    