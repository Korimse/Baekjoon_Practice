from collections import deque

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
def bfs(arr):
  queue = deque()
  queue.append(arr)
  while queue:
    x1, y1, x2, y2 = queue.popleft()
    if dist[x1][y1][x2][y2] > 10:
      break
    for i in range(4):
      nx1 = x1 + dx[i]
      ny1 = y1 + dy[i]
      nx2 = x2 + dx[i]
      ny2 = y2 + dy[i]
      if graph[nx1][ny1] == 0 and graph[nx2][ny2] == 0:
        continue
      if graph[nx1][ny1] == 0:
        return dist[x1][y1][x2][y2]
      if graph[nx2][ny2] == 0:
        return dist[x1][y1][x2][y2]
      if graph[nx1][ny1] == '#':
        nx1, ny1 = x1, y1
      if graph[nx2][ny2] == '#':
        nx2, ny2 = x2, y2
      if not dist[nx1][ny1][nx2][ny2]:
        dist[nx1][ny1][nx2][ny2] = dist[x1][y1][x2][y2] + 1
        queue.append([nx1, ny1, nx2, ny2])
  return -1

n, m = map(int, input().split(' '))
graph = [[0]*(m+2)]
for i in range(n):
  graph.append([0]+list(input())+[0])
graph.append([0]*(m+2))

arr = []
for i in range(n+2):
  for j in range(m+2):
    if graph[i][j] == 'o':
      arr.append(i)
      arr.append(j)
dist = [[[[0]*(m+2) for _ in range(n+2)] for _ in range(m+2)] for _ in range(n+2)]
dist[arr[0]][arr[1]][arr[2]][arr[3]] = 1
print(bfs(arr))
