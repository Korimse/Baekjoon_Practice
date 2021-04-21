from collections import deque

n, m = map(int, input().split())

graph = []
visited = [[0]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph, x, y):
    graph[x][y] = 0
    visited[x][y] = 1
    cnt = 1

    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
    return cnt

result = []
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
           result.append(bfs(graph, i, j))
           answer += 1

print(answer)
if len(result) == 0:
    print(0)
else:
    print(max(result))