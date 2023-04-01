science=[]
social=[]

for i in range(4):
    science.append(int(input()))

for i in range(2):
    social.append(int(input()))

science.sort(reverse=True)
social.sort(reverse=True)

print(science[0]+science[1]+science[2]+social[0])
