angle=[]
for i in range(3):
    angle.append(int(input()))

if angle[0]==60 and angle[1]==60 and angle[2]==60:
    print("Equilateral")

elif sum(angle)==180 and angle[0]==angle[1]:
    print("Isosceles")
elif sum(angle)==180 and angle[1]==angle[2]:
    print("Isosceles")
elif sum(angle)==180 and angle[0]==angle[2]:
    print("Isosceles")

elif sum(angle)==180 and angle[0]!=angle[1] and angle[1]!=angle[2] and angle[0]!=angle[2]:
    print("Scalene")

elif sum(angle)!=180:
    print("Error")