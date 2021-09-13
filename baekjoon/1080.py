n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(input()))
brr = []
for i in range(n):
    brr.append(list(input()))


def change(x,y):
    for a in range(x,x+3):
        for b in range(y,y+3):
            if arr[a][b] == '1':
                arr[a][b] = '0'
            else:
                arr[a][b] = '1'
answer = 0

for i in range(n-2):
    for j in range(m-2):
        if arr[i][j] != brr[i][j]:
            change(i,j)
            answer += 1

if arr == brr:
    print(answer)
else:
    print(-1)