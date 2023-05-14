h,m,s = map(int,input().split())
d = int(input()) # 초 단위

# 1번째
s1 = (s+d)%60  #최종 초
m1 = (s+d)//60

# 2번째
m2 = (m+m1)%60 # 최종 분
h1 = (m+m1)//60

# 3번째
h2 = (h+h1)%24 # 최종 시각

print(h2,m2,s1)  #출력