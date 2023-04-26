t=int(input())

for i in range(t):
    count=int(input()) #124
    quarter=count//25 #4
    count=count%25
    dime=count//10 #2
    count=count%10
    nickel=count//5 #0
    count=count%5
    pennie=count #4
    print(quarter, dime, nickel, pennie)