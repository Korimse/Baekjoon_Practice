from collections import deque
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
graph = [[] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      graph[i].append(j)

def bfs(graph, start):
  visited = [0]*n
  queue = deque()
  queue.append(start)
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        visited[i] = 1
        queue.append(i)
  return visited
answer = []
for i in range(n):
  answer.append(bfs(graph, i))

for i in answer:
  print(*i)