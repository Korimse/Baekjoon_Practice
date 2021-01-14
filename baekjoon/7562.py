from collections import deque

dx = [-2, -2, -1, -1, 2, 2, 1, 1]
dy = [-1, 1, 2, -2, 1, -1, 2, -2]

def bfs(i, j, ex, ey):
  queue = deque()
  queue.append((i,j))

  while queue:
    a, b = queue.popleft()
    for i in range(8):
      x = a+dx[i]
      y = b + dy[i]
      if 0<=x<n and 0<=y<n and arr[x][y] == 0:
        arr[x][y] = arr[a][b]+1
        if x == ex and y == ey:
          break
        queue.append((x, y))
k = int(input())
for _ in range(k):
  n = int(input())
  arr = [[0]*n for _ in range(n)]
  sx, sy = map(int, input().split())
  ex, ey = map(int, input().split())
  if (sx, sy) == (ex, ey):
    print(0)
  else:
    bfs(sx, sy, ex, ey)
    print(arr[ex][ey])
