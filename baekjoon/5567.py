from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [0]*(n+1)

def bfs():
  queue = deque()
  queue.append(1)
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        visited[i] = visited[v] + 1
        queue.append(i)

bfs()
answer = 0
for i in range(2, len(visited)):
  if visited[i] == 1 or visited[i] == 2:
    answer += 1
print(answer)
