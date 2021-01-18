import sys
from collections import deque

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())

def bfs(x, y):
  queue = deque()
  queue.append((x, y, 0))
  visited = [[[0]*2 for i in range(m)] for i in range(n)]
  visited[x][y][0] = 1
  while queue:
    a, b, c = queue.popleft()
    if a == n-1 and b == m-1:
      return visited[a][b][c]
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if c == 0 and graph[nx][ny] == 1:
          visited[nx][ny][1] = visited[a][b][c] + 1
          queue.append((nx, ny, 1))
        elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
          visited[nx][ny][c] = visited[a][b][c] + 1
          queue.append((nx, ny, c))
  return -1

graph = []
for i in range(n):
  graph.append(list(map(int, list(input().strip()))))

print(bfs(0, 0))
