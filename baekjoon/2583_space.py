from collections import deque

m, n, k = map(int, input().split())
s = [[0] * n for i in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = []
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            s[j][k] = 1
result = []
def bfs(i, j):
  global result
  count = 1
  queue = deque()
  queue.append((i, j))
  s[i][j] = 1
  while queue:
    a, b = queue.popleft()

    for i in range(4):
      x = a + dx[i]
      y = b + dy[i]

      if 0<=x<m and 0<=y<n and s[x][y] == 0:
        s[x][y] = 1
        queue.append((x, y))
        count += 1
  result.append(count)

for i in range(m):
  for j in range(n):
    if s[i][j] == 0:
      bfs(i, j)
result = sorted(result)
print(len(result))
print(*result)
