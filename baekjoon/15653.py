from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
  cnt = 0
  while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
    x = x + dx
    y = y + dy
    cnt += 1
  return x, y, cnt

for i in range(n):
  for j in range(m):
    if graph[i][j] == 'R':
      rx, ry = i, j
    elif graph[i][j] == 'B':
      bx, by = i, j

visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

def bfs():
  queue = deque()
  queue.append((rx, ry, bx, by, 1))
  while queue:
    ra, rb, ba, bb, r = queue.popleft()
    visited[ra][rb][ba][bb] = 1
    for i in range(4):
      nrx, nry, rcnt = move(ra, rb, dx[i], dy[i])
      nbx, nby, bcnt = move(ba, bb, dx[i], dy[i])
      if graph[nbx][nby] == 'O':
        continue
      if graph[nrx][nry] == 'O':
        print(r)
        return True
      if nrx == nbx and nry == nby:
        if rcnt > bcnt:
          nrx -= dx[i]
          nry -= dy[i]
        else:
          nbx -= dx[i]
          nby -= dy[i]
      if visited[nrx][nry][nbx][nby] == 0:
        visited[nrx][nry][nbx][nby] = 1
        queue.append((nrx, nry, nbx, nby, r+1))
  return False

if bfs() == False:
  print(-1)
