def divisor(n):
    arr=[]

    for i in range(1,n+1):
        if n % i ==0:
            arr.append(i)
    print(arr)

# divisor(6) [1, 2, 3, 6]


while (1):
    n=int(input())

    if n==-1:
        break
    else:
        arr=[]
        for i in range(1, n):
            if n%i==0:
                arr.append(i)
        
        if sum(arr)==n:
            print(n, ' = ', " + ".join(str(i) for i in arr), sep="")
        else:
            print(n, "is NOT perfect.")