import sys

n=int(sys.stdin.readline()) #5

a_list=list(map(int, input().split()))
b_list=list(map(int, input().split()))

# 방법1: 둘 다 sort 해서 가장 큰 수 * 가장 작은 수st로 풀기
"""
sorted_a_list=sorted(a_list)
sorted_b_list=sorted(b_list)

s=0
for i in range(n):
    s += sorted_a_list[i] * sorted_b_list[n-i-1]
"""

# 방법2: sort 없이 max, min을 사용해서 가장 큰 수 * 가장 작은 수st로 풀기
s=0
for i in range(n):
    s += max(a_list) * min(b_list)
    a_list.pop(a_list.index(max(a_list)))
    b_list.pop(b_list.index(min(b_list)))

print(s)