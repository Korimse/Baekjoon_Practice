from collections import deque
n = int(input())

arr = []
for i in range(n):
  arr.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr, x, y, v):
  queue = deque()
  queue.append((x, y))
  arr[x][y] = 0
  while queue:
    a, b = queue.popleft()

    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if 0<=nx<n and 0<=ny<n and arr[nx][ny] == v:
        queue.append((nx, ny))
        arr[nx][ny] = 0
answer = 0
answer1 = 0
copy = [[0]*n for i in range(n)]
for i in range(n):
  for j in range(n):
    if arr[i][j] == 'G':
      copy[i][j] = 'R'
    else:
      copy[i][j] = arr[i][j]

for i in range(n):
  for j in range(n):
    if arr[i][j] != 0:
      bfs(arr, i, j, arr[i][j])
      answer += 1
    if copy[i][j] != 0:
      bfs(copy, i, j, copy[i][j])
      answer1 += 1
print(answer, answer1)