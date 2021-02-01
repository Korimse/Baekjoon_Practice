from collections import deque

n = int(input())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))
visited = [[-1]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  queue = deque()
  queue.append((0,0))
  visited[0][0] = 0
  while queue:
    a, b = queue.popleft()
    if a == n-1 and b == n-1:
      print(visited[a][b])
      return
    for i in range(4):
      x = a + dx[i]
      y = b + dy[i]

      if 0<=x<n and 0<=y<n:
        if visited[x][y] == -1:
          if graph[x][y] == 1:
            visited[x][y] = visited[a][b]
            queue.appendleft((x, y))
          else:
            visited[x][y] = visited[a][b] + 1
            queue.append((x, y))
    for i in visited:
      print(i)
    print()
bfs()
