from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

parent = [0]*(n+1)
def bfs(graph, start, parent):
  queue = deque()
  queue.append(start)
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if parent[i] == 0:
        parent[i] = v
        queue.append(i)

bfs(graph, 1, parent)
for i in range(2, len(parent)):
  print(parent[i])
