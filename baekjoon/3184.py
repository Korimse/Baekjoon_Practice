from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(m)] for _ in range(n)]
def bfs(x, y):
  sheep = 0
  wolf = 0
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1
  if graph[x][y] == 'o':
    sheep += 1
  elif graph[x][y] == 'v':
    wolf += 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and graph[nx][ny] != '#' and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        if graph[nx][ny] == 'o':
          sheep += 1
        elif graph[nx][ny] == 'v':
          wolf += 1
        queue.append((nx, ny))
  if wolf >= sheep:
    sheep = 0
  else:
    wolf = 0
  return sheep, wolf
s = 0
w = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] != '#' and visited[i][j] == 0:
      a, b = bfs(i, j)
      s += a
      w += b

print(s, w)
