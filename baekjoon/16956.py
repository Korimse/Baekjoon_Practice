n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

isClear = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<n and 0<=ny<m:
                    if graph[nx][ny] == 'S':
                        isClear = False
if isClear == False:
    print(0)
else:
    print(1)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                graph[i][j] = 'D'
    for g in graph:
        print(''.join(g))