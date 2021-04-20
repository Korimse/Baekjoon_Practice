from collections import deque

dx = [0,0,-1,1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

def bfs(graph, x, y):
    graph[x][y] = 0

    queue = deque()
    queue.append((x, y))
    while queue:
        x,y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
        

while True:
    m, n = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = []
    cnt = 0

    for i in range(n):
        graph.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)