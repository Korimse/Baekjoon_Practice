from collections import deque
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def safe_place(copy):
  answer = 0
  for i in range(n):
    for j in range(n):
      if copy[i][j] != 0:
        bfs(copy, i, j)
        answer += 1
  return answer

def bfs(copy, x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n:
        if copy[nx][ny] != 0:
          copy[nx][ny] = 0
          queue.append((nx, ny))
          

minv = 101
maxv = 0
for i in range(n):
  for j in range(n):
    minv = min(minv, arr[i][j])
    maxv = max(maxv, arr[i][j])

for i in range(0, 101):
  copy = [[0]*n for _ in range(n)]
  for j in range(n):
    for k in range(n):
      if arr[j][k] > i:
        copy[j][k] = arr[j][k]
  cnt = safe_place(copy)
  if cnt == 0:
    break

  answer = max(answer, cnt)

print(answer)
