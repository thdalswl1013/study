"""
stable 정렬: [1, 2, 3(X), 4, 5, 3(Y)] 을 오름차순 정렬한다면,
             [1, 2, 3(X), 3(Y), 4, 5]순으로 3끼리의 위치가 바뀌지 않음
"""

n = int(input())
arr = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name))

arr.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for i in range(n):
    print(arr[i][0], arr[i][1])