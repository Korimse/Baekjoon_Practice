from collections import deque

t = int(input())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))


for _ in range(t):
    n, m, k = map(int, input().split())
    cnt = 0

    graph = [[0]*m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)