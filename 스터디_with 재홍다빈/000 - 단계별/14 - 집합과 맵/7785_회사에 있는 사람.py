n = int(input())
arr = {}

for i in range(n):
    name, enter_leave = map(str, input().split())

    if enter_leave == 'enter':
        arr[name] = '1'

    elif enter_leave == 'leave':
        del arr[name]

arr = sorted(arr.keys(), reverse = True)

for i in arr:
    print(i)
