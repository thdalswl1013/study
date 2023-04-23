n=int(input())

box1 = n // 5
box2 = n % 5

while True:
    if box2 % 3 != 0: # 3으로 나눠지지않으면
        box1 -= 1 # box1에서 5kg 빼고, 5kg만큼 box2로 옮겨줌
        box2 += 5

        if box1 < 0:
            print(-1)
            break
 
    else:
        box2 //= 3
        print(box1 + box2)
        break