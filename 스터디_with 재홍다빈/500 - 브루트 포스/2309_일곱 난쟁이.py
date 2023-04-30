height=[]
sum=0
for i in range(9):
    height.append(int(input()))
    sum+=height[i]


height.sort()

for i in range(9):
    for j in range(i+1, 9):
        if height[i] + height[j] == sum - 100:

            for k in range(9):
                if k == i or k == j:
                    pass

                else:
                    print(height[k])
                    
            exit()
            
print(height)
