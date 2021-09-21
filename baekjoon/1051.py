n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

ms = min(n, m)
answer = 0
for s in range(2, ms+1):
    for i in range(n-s+1):
        for j in range(m-s+1):
            a, b, c, d = (i,j), (i+s-1, j), (i, j+s-1), (i+s-1, j+s-1)
            if arr[a[0]][a[1]] == arr[b[0]][b[1]] == arr[c[0]][c[1]] == arr[d[0]][d[1]]:
                answer = max(answer, s*s)

if answer == 0:
    print(1)
else:
    print(answer)