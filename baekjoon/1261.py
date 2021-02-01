from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(m):
  graph.append(input())
visited = [[-1]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
  queue = deque()
  queue.append((0,0))
  visited[0][0] = 0
  while queue:
    a, b = queue.popleft()
    for i in range(4):
      x = a + dx[i]
      y = b + dy[i]
      if 0<=x<m and 0<=y<n:
        if visited[x][y] == -1:
          if graph[x][y] == '0':
            queue.appendleft((x, y))
            visited[x][y] = visited[a][b]
          else:
            queue.append((x, y))
            visited[x][y] = visited[a][b] + 1
  print(visited[m-1][n-1])

bfs()