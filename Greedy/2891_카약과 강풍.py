#어렵..

n, s, r = map(int,input().split())
team_damaged = list(map(int, input().split()))
team_surplus = list(map(int, input().split()))
boat = [0]*n

for i in team_damaged:
    boat[i-1] -= 1
for i in team_surplus:
    boat[i-1] += 1

result = []
    
for i in boat:
    if result:
        if i == -1:
            if result[-1] == 1:
                result.pop()
            else:
                result.append(i)

        elif i == 1:
            if result[-1] == -1:
                result.pop()
            else:
                result.append(i)
            
        else:
            result.append(i)

    else:
        result.append(i)

print(result.count(-1)) #스택에서 -1의 개수를 구해라


# 실패1
"""
n, s, r = map(int, input().split()) # 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R

team_damaged=list(map(int, input().split())) # 카약이 손상된 팀의 번호
team_surplus=list(map(int, input().split())) # 카약을 하나 더 가져온 팀의 번호

team_damaged.sort()
team_surplus.sort()

result=s

for i in range(s):
    if not team_surplus:
        break
    
    for j in range(r):
        if team_damaged[i] == team_surplus[j] or team_damaged[i] == team_surplus[j]+1 or team_damaged[i] == team_surplus[j]-1:
            result-=1
            team_surplus[j]=-1
            break

print(result)
"""

# 실패2
"""
n, s, r = map(int, input().split()) # 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R

team_damaged=list(map(int, input().split())) # 카약이 손상된 팀의 번호
team_surplus=list(map(int, input().split())) # 카약을 하나 더 가져온 팀의 번호

result = 0

for i in team_damaged: # 출발하지 못하는 팀은 카약이 손상된 팀 중에 있음

    if i-1 in team_surplus: # 카약이 손상된 팀 앞뒤에 카약이 남는 팀이 있으면, 카약을 빌릴 수 있음
        team_surplus.remove(i-1) # 남는 팀 리스트에서 해당 팀을 삭제하면 됨
    
    elif i+1 in team_surplus:
        team_surplus.remove(i+1)
    
    else: # 카약을 빌릴 팀이 없다면
        result+=1


# 출발할 수 없는 팀의 최솟값 출력
print(result)

"""