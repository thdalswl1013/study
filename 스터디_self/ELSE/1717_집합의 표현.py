
import sys
sys.setrecursionlimit(10**6)


# a가 속한 집합과 b가 속한 집합 합치기
def union(x, y):
    x = parent(x)
    y = parent(y)

    # a와 b의 부모 노드가 같으면 동일한 집합이므로 리턴
    if x == y:
        return
    # 부모 노드가 다르다면 두 집합을 합친다.
    else:
        nums[y] = x


# 부모 노드 찾기
def parent(target):
    # 자기 자신이 부모 노드이면 자기 자신을 리턴
    if target == nums[target]:
        return target

    # 부모 노드를 재귀함수를 통해 찾는다.
    nums[target] = parent(nums[target])

    # 자신의 부모 노드를 리턴
    return nums[target]


n, m = map(int, sys.stdin.readline().split())
nums = [i for i in range(n + 1)]

for _ in range(m):
    k, a, b = map(int, sys.stdin.readline().split())

    # a가 포함되어 있는 집합과 b과 포함되어 있는 집합을 합친다.
    if k == 0:
        union(a, b)

    # a와 b가 같은 집합에 포함되어 있는지 확인한다.
    else:
        # 부모 노드가 같으면 yes를 출력
        if parent(a) == parent(b):
            print("YES")

        # 다르면 no를 출력
        else:
            print("NO")
