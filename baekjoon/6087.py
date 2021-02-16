from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph= []
for i in range(m):
  graph.append(list(input().strip()))

c = []
for i in range(m):
  for j in range(n):
    if graph[i][j] == 'C':
      c.append((i, j))

visited = [[0]*n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((c[0][0], c[0][1]))
while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    while 0<=nx<m and 0<=ny<n and graph[nx][ny] != '*':
      if visited[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))
      nx += dx[i]
      ny += dy[i]

print(visited[c[1][0]][c[1][1]]-1)
