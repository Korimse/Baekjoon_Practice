from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [list(input()) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
  queue = deque()
  queue.append((0, 0, 0))
  visited[0][0][0] = 1
  while queue:
    x, y, d = queue.popleft()
    if x == n-1 and y == m-1:
      return visited[x][y][d]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      nd = d+1
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if visited[nx][ny][d]:
        continue
      if graph[nx][ny] == '0':
        visited[nx][ny][d] = visited[x][y][d] + 1
        queue.append((nx, ny, d))
      if graph[nx][ny] == '1' and nd <= k:
        visited[nx][ny][nd] = visited[x][y][d] + 1
        queue.append((nx, ny, nd))
  return -1
print(bfs())
