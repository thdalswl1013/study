#어려웠엉,,

m, n = map(int, input().split())
dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six','7':'seven', '8':'eight', '9':'nine', '0':'zero'}

arr=[]
for i in range(m, n+1):
    s=''.join([dict[j] for j in str(i)])
    arr.append([i, s])

arr.sort(key=lambda x: x[1])

for i in range(len(arr)):
    if i%10==0 and i!=0: # 한 줄에 열 개씩 출력
        print()
    print(arr[i][0], end=' ')