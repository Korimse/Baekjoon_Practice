from collections import deque

def bfs():
  count = 0
  while queue:
    qu = len(queue)
    while qu:
      v = queue.popleft()
      for i in range(4):
        x = v[0] + dx[i]
        y = v[1] + dy[i]
        if x >= 0 and x < h and y >= 0 and y < w:
          if visited[x][y] != 1 and visited[x][y] < visited[v[0]][v[1]]:
            visited[x][y] = 9
            queue.append((x, y))
        elif x < 0 or y < 0 or x >= h or y >= w:
          print(count+1)
          return
      qu = qu - 1
    fire()
    count += 1
  
  print("IMPOSSIBLE")
  return
    
def fire():
  q = len(fqueue)
  while q:
    v = fqueue.popleft()
    visited[v[0]][v[1]] = 1
    for i in range(4):
      x = v[0] + dx[i]
      y = v[1] + dy[i]
      if 0 <= x < h and 0 <= y < w and visited[x][y] == 0:
        visited[x][y] = 1
        fqueue.append((x, y))
    q -= 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())

for i in range(n):
  w, h = map(int, input().split())
  graph = []
  visited = [[0]*w for _ in range(h)]
  for j in range(h):
    graph.append(list(input()))
    for k in range(w):
      visited[j][k] = graph[j][k]
  queue = deque()
  fqueue = deque()
  
  for j in range(h):
    for k in range(w):
      if graph[j][k] == '.':
        visited[j][k] = 0
      if graph[j][k] == '#':
        visited[j][k] = 1
      if graph[j][k] == '*':
        fqueue.append((j, k))
        visited[j][k] = 1
      if graph[j][k] == '@':
        queue.append((j, k))
        visited[j][k] = 9
  fire()
  bfs()
