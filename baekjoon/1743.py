from collections import deque

n, m, k = map(int, input().split())

graph = [[0]*m for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    queue.append((nx, ny))
                
    return cnt

answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer.append(bfs(graph, i,j))

print(max(answer))
                