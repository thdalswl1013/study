a, p =map(int,input().split())
"""
57
5*5+7*=74
7*7+4*4=65
6*6+5*5=61
...
"""

numArr=[a]
while True:
    temp=0
    for i in str(numArr[-1]):
        temp+=int(i) **p
    
    if temp in numArr:
        break

    numArr.append(temp)

print(numArr.index(temp))