n=int(input())

cute=0 # 1
uncute=0 # 0

for i in range(n):
    x=int(input())
    if x==1:
        cute+=1
    elif x==0:
        uncute+=1
    
#print(cute, uncute)

if cute<uncute:
    print("Junhee is not cute!")
elif cute>uncute:
    print( "Junhee is cute!")