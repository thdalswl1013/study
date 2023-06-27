# 100점 답안
t = int(input())

if t % 10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = t // 300
    b = (t % 300) // 60
    c = (t % 300) % 60 // 10
    print(a, b, c)



# 30점 답안
"""
t=int(input())

# a: 300초, b: 60초, c: 10초
if t%10!=0:
    print(-1)

elif t//300>0:
    a=t//300
    t=t%300
    
    if t//60>0:
        b=t//60
        c=t%60
        c=c//10
    print(a,b,c)

elif t//300==0:
    a=0
    b=t//60
    c=t%60
    c=c//10

    print(a,b,c)

"""