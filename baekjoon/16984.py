from collections import deque

n = int(input())

sx, sy, ex, ey = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
visited = [[-1 for _ in range(n)] for _ in range(n)]
visited[sx][sy] = 0
queue = deque()
queue.append((sx, sy))
while queue:
  a, b = queue.popleft()
  for i in range(6):
    x = a + dx[i]
    y = b + dy[i]
    if 0<=x<n and 0<=y<n:
      if visited[x][y] == -1:
        visited[x][y] = visited[a][b] + 1
        queue.append((x, y))

if visited[ex][ey] > -1:
  print(visited[ex][ey])
else:
  print(-1)
