n, k = map(int, input().split())

arr = []
di = [[0 for _ in range(k+1)] for _ in range(n)]

for i in range(n):
    w, v = map(int, input().split())
    arr.append([w,v])

for i in range(n):
    for j in range(k+1):
        weight = arr[i][0]
        value = arr[i][1]

        if j < weight:
            di[i][j] = di[i-1][j]
        else:
            di[i][j] = max(value + di[i-1][j-weight], di[i-1][j])

print(di[n-1][k])