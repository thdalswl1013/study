v=int(input())
vote=input()
arr=[]

"""
for i in vote:
    arr.append(i)
print(arr)
"""
a_cnt=0
b_cnt=0
for i in vote:
    if i=='A':
        a_cnt+=1
    elif i=="B":
        b_cnt+=1

if a_cnt<b_cnt:
    print("B")
elif a_cnt>b_cnt:
    print("A")
else:
    print("Tie")