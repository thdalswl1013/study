# 알파벳 개수를 구하는 과정
baekjoon = list((input()))
alphabet="abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    cnt = baekjoon.count(alphabet[i])
    print(cnt, end=' ')

# 알파벳 유무를 구하는 과정
"""
baekjoon=input()
alphabet="abcdefghijklmnopqrstuvwxyz"
arr=[]
for i in alphabet:
    if i in baekjoon:
        arr.append(1)
    elif i not in baekjoon:
        arr.append(0)


for i in range(len(arr)):
    print(arr[i], end=' ')

"""