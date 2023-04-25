while(1):
    x,y=map(int,input().split())

    if x==0 and y==0:
        break

    if x>y and x%y==0:
            print("multiple")
    elif x<y and y%x==0:
            print("factor")

    else:   
        print("neither")
    
    
        
