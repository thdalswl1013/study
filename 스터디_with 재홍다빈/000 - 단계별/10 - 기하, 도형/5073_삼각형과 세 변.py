while(1):
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    
    elif (max(a,b,c)==c and a+b<=c) or (max(a,b,c)==b and a+c<=b) or (max(a,b,c)==a and b+c<=a):
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif (a==b and b!=c) or (a!=b and a==c) or (a!=c and b==c):
        print("Isosceles")
    elif  a!=b and b!=c and a!=c:
        print("Scalene")