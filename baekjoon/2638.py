from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    queue.append((0,0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] >= 1:
                        graph[nx][ny] += 1
                    else:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
answer = 0

while True:
    bfs()
    isValid = False

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                isValid = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    
    if isValid == True:
        answer += 1
    else:
        break
print(answer)