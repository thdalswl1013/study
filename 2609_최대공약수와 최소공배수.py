x,y=map(int, input().split())

for i in range(min(x,y),0,-1):
    if x%i==0 and y%i==0:
        print(i)
        break

for j in range(max(x,y), (x*y)+1): 
    if j%x==0 and j%y==0:
        print(j)
        break
