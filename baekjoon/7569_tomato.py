from collections import deque

m, n, h = map(int, input().split())
s = [[] for i in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

queue = deque()
isTrue = False
for i in range(h):
  for j in range(n):
    s[i].append(list(map(int, input().split())))

for z in range(h):
  for x in range(n):
    for y in range(m):
      if s[z][x][y] == 1:
        queue.append((x, y, z))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
  while queue:
    a, b, c = queue.popleft()
    visited[c][a][b] = 1
    for i in range(6):
      x = a + dx[i]
      y = b + dy[i]
      z = c + dz[i]
      if 0<=x<n and 0<=y<m and 0<=z<h and s[z][x][y] == 0 and visited[z][x][y] == 0:
        queue.append((x, y, z))
        s[z][x][y] = s[c][a][b] + 1
        visited[z][x][y] = 1

bfs()
maxv = 0
for z in range(h):
  for x in range(n):
    for y in range(m):
      if s[z][x][y] == 0:
        isTrue = True
      maxv = max(maxv, s[z][x][y])
if isTrue == True:
  print(-1)
else:
  print(maxv-1)
