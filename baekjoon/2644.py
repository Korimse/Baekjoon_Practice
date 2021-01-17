from collections import deque

n = int(input())
x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
m = int(input())
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [0]*(n+1)

def bfs(x, y):
  queue = deque()
  queue.append(x)
  while queue:
    v = queue.popleft()
    visited[x] = 1
    for i in graph[v]:
      if visited[i] == 0:
        visited[i] = visited[v] + 1
        queue.append(i)
bfs(x, y)
print(visited[y]-1)