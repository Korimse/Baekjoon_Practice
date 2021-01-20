from collections import deque
import sys
input = sys.stdin.readline
k = int(input())
def bfs(i):
  global isTrue
  queue = deque()
  queue.append(i)
  visited[i] = 1
  while queue:
    v = queue.popleft()
    for s in graph[v]:
      if visited[s] == 0:
        if visited[v] == 1:
          visited[s] = -1
          queue.append(s)
        elif visited[v] == -1:
          visited[s] = 1
          queue.append(s)
      elif visited[v] == visited[s]:
        return 1
  return 0

for _ in range(k):
  n, m = map(int, input().split())
  graph = [[] for i in range(n+1)]
  for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


  visited = [0]*(n+1)
  isTrue = True

  for i in range(1, n+1):
    if visited[i] == 0:
      ans = bfs(i)
      if ans == 1:
        break
  if ans == 1:
    print("NO")
  else:
    print("YES")