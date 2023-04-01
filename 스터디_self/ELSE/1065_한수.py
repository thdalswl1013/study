n=int(input())

# 1~n 사이의 한수 개수를 구해라

if n<100:
    print(n)

else:
    cnt=99
    for i in range(100, n+1):
        i = str(i)

        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            cnt+=1

    print(cnt)