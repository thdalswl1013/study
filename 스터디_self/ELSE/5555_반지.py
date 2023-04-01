
str=input() # 문자열
n=int(input()) # 반지 개수

str_arr=[]
for i in range(n):
    str_arr.append(input())

cnt=0
for i in range(n):
    str_arr[i]=str_arr[i]*2

    if str in str_arr[i]:
        cnt+=1

print(cnt)


# 틀렸는데, 왜 틀린지 모르겠음.. 예제 답은 맞았었는디..
"""
str=input() # 문자열
n=int(input()) # 반지 개수

str_arr=[]
for i in range(n):
    str_arr.append(input())

cnt=0
str_front= str.replace(str[-1],'')

for i in range(n):
    if str in str_arr[i] or (str[-1]==str_arr[i][0] and str_front in str_arr[i]):
        cnt+=1

print(cnt)
"""