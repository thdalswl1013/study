a, b = map(int, input().split())

alist=list(map(int, input().split()))
blist=list(map(int, input().split()))

one=set(alist) - set(blist)
two=set(blist) - set(alist)

print(len(one)+len(two))