n=int(input())
dic={}

for i in range(n):
    sell=input()

    if sell not in dic:
        dic[sell]=1
    else:
        dic[sell]+=1

#print(dic) # {'top': 4, 'kimtop': 1}

arr=[]
num=max(dic.values()) # 4

for i in dic:
    if num==dic[i]:
        arr.append(i)

arr.sort()
print(arr[0])

# 답이 틀림 -> 왜?
"""
n=int(input())
sell=[]

for i in range(n):
    sell.append(input()) # top top top top kimtop

sell_count=[]
for i in range(n):
    sell_count.append(sell.count(sell[i])) # 4 4 4 4 1

for i in range(n):
    if sell_count[i]==max(sell_count): 
        print(sell[i])
        break

"""