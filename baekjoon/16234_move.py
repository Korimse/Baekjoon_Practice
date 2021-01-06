from collections import deque

n, l, r = map(int, input().split())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  queue = deque()
  queue.append((i, j))
  tmp = []
  tmp.append((i, j))
  while queue:
    a, b = queue.popleft()
    
    for i in range(4):
      x = a + dx[i]
      y = b + dy[i]
      
      if 0<=x<n and 0<=y<n and visited[x][y] == 0:
        if l <= abs(arr[x][y]-arr[a][b]) <= r:
          queue.append((x, y))
          tmp.append((x, y))
          visited[x][y] = 1
  return tmp
cnt = 0
while True:
  visited = [[0] * n for i in range(n)]
  isTrue = False
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0:
        visited[i][j] = 1
        temp = bfs(i, j)
        if len(temp) > 1:
          isTrue = True
          num = 0
          for x, y in temp:
            num += arr[x][y]
          num = num // len(temp)
          for x, y in temp:
            arr[x][y] = num
  if isTrue == False:
    break
  cnt += 1
print(cnt)