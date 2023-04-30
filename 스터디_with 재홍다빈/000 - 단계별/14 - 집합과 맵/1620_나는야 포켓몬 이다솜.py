
n, m = map(int, input().split())
dic_int_key = {}  # Key값이 int인 dictionary
dic_str_key = {}  # Key값이 str인 dictionary
for i in range(n):
    name = input().strip()
    dic_int_key[i] = name
    dic_str_key[name] = i

# 포켓몬 탐색
for _ in range(m):
    item =input().strip()
    if item.isdigit() == True:  # isdigit -> O(n)
        print(dic_int_key[int(item)-1])
    else:
        print(dic_str_key[item]+1)

# 시간초과
"""
n, m = map(int, input().split())
dic_int_key = {}  # Key값이 int인 dictionary
dic_str_key = {}  # Key값이 str인 dictionary
for i in range(n):
    name = input().strip()
    dic_int_key[i] = name
    dic_str_key[name] = i

# 포켓몬 탐색
for _ in range(m):
    item =input().strip()
    if item.isdigit() == True:  # isdigit -> O(n)
        print(dic_int_key[int(item)-1])
    elif item.isdigit() == False:
        print(dic_str_key[item]+1)


"""

#시간 초과
"""
n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(input())


for i in range(n):
    x=input()
    if str.isdigit(x)==True:
        print(arr[int(x)-1])
    elif str.isdigit(x)==False:
        print(arr.index(x)+1)

"""