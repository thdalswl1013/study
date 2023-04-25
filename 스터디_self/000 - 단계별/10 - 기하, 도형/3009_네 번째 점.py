xList=[]
yList=[]

for i in range(3):
    x,y=map(int,input().split())
    xList.append(x)
    yList.append(y)

for i in range(3):
    if xList.count(xList[i])==1:
        x4=xList[i]
    if yList.count(yList[i])==1:
        y4=yList[i]


print(x4, y4)


# 런타임 에러
"""
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
if x1==x2:
    x4=x3

elif x1==x3:
    x4=x2

elif x2==x3:
    x4=x1


if y1==y2:
    y4=y3

elif y1==y3:
    y4=y2

elif x2==y3:
    y4=y1

print(x4, y4)

"""