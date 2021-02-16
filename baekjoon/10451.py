from collections import deque
import sys

input = sys.stdin.readline

def bfs(start, end):
  queue = deque()
  queue.append(start)
  visited[start] = 1
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if i == end:
        return True
      if visited[i] == 0:
        visited[i] = 1
        queue.append(i)
  return False


k = int(input())
for _ in range(k):
  n = int(input())
  answer = 0
  arr = list(map(int, input().split()))
  graph = [[] for _ in range(n+1)]
  for i in range(len(arr)):
    graph[i+1].append(arr[i])
  visited = [0]*(n+1)
  for i in range(1, n+1):
    if bfs(i, i) == True:
      answer += 1
  print(answer)
