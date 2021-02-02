from collections import deque

n = int(input())

emoji = 1
clip = 0
queue = deque()
queue.append((1, 0))
visited = [[-1]*1001 for _ in range(1001)]
visited[1][0] = 0
while queue:
  c, v = queue.popleft()
  
  if visited[c][c] == -1:
    visited[c][c] = visited[c][v] + 1
    queue.append((c, c))
  if c + v <= n and visited[c+v][v] == -1:
    visited[c+v][v] = visited[c][v] + 1
    queue.append((c+v, v))
  if c-1>=0 and visited[c-1][v] == -1:
    visited[c-1][v] = visited[c][v] + 1
    queue.append((c-1, v))

r = visited[n][1]
for i in range(1, n):
  if visited[n][i] != -1:
    r = min(r, visited[n][i])
print(r)
