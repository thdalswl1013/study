# 풀이 1
a,b,c=map(int, input().split())

if max(a,b,c)==a:
    print(max(b,c))

elif max(a,b,c)==b:
    print(max(a,c))

elif max(a,b,c)==c:
    print(max(a,b))


# 풀이 2
"""
arr=list(map(int, input().split()))
arr.sort()
print(arr[1])
"""