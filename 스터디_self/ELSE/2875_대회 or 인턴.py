# n: 여학생 m: 남학생 k:인턴십 참여 인원
n, m, k=map(int,input().split())

# 여2 남1
team = 0

while(1):
    n-=2
    m-=1

    if n<0 or m<0 or (n+m)<k:
        break
    team+=1

print(team)