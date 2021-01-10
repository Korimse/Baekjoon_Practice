from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
  queue = deque()
  queue.append((sx, sy, sz))
  while queue:
    a, b, c = queue.popleft()
    for i in range(6):
      x = a + dx[i]
      y = b + dy[i]
      z = c + dz[i]
      if 0<=x<m and 0<=y<k and 0<=z<n and visited[z][x][y] == 0:
        if arr[z][x][y] == '.' or arr[z][x][y] == 'E':
          visited[z][x][y] = 1
          dp[z][x][y] = dp[c][a][b] + 1
          queue.append((x, y, z))

    

while True:
  n, m, k = map(int, input().split())
  if n == 0 and m == 0 and k == 0:
    break
  arr = [[] for _ in range(n)]
  for i in range(n):
    for j in range(m):
      arr[i].append(list(map(str, input())))
    input()
  visited = [[[0]*k for i in range(m)] for i in range(n)]
  dp = [[[0]*k for i in range(m)] for i in range(n)]
  for i in range(n):
    for j in range(m):
      for l in range(k):
        if arr[i][j][l] == 'S':
          sx, sy, sz = j, l, i
        elif arr[i][j][l] == 'E':
          ex, ey, ez = j, l, i
  bfs()
  if dp[ez][ex][ey] == 0:
    print("Trapped!")
  else:
    print("Escaped in %d minute(s)." % dp[ez][ex][ey])
