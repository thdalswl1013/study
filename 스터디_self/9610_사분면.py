n=int(input())

first=0
second=0
third=0
fourth=0
axis=0

for i in range(n):
    x,y=map(int,input().split())

    if x>0 and y>0:
        first+=1
    elif x<0 and y>0:
        second+=1
    elif x<0 and y<0:
        third+=1
    elif x>0 and y<0:
        fourth+=1
    else:
        axis+=1
         

print("Q1:", first)
print("Q2:", second)
print("Q3:", third)
print("Q4:", fourth)
print("AXIS:", axis)