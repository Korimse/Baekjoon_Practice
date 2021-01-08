from collections import deque
n, m = map(int, input().split())
graph= []
for i in range(n):
  graph.append(list(map(int, input().split())))

def bfs_o(che):
  queue = deque()
  queue.append((0, 0))
  visited[0][0] = 1
  while queue:
    a, b = queue.popleft()
    for i in range(4):
      x = a + dx[i]
      y = b + dy[i]
      if 0<=x<n and 0<=y<m and visited[x][y] == 0:
        visited[x][y] = 1
        if graph[x][y] == 1:
          graph[x][y] = 2
          che -= 1
        else:
          queue.append((x, y))
  return che

def resett():
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2:
        graph[i][j] = 0

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
che = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      che += 1

num = che

while True:
  visited = [[0]*m for _ in range(n)]
  che = bfs_o(che)
  answer += 1
  resett()
  if che != 0:
    num = che
  else:
    break

print(answer)
print(num)