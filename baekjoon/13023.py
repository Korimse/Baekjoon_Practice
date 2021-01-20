n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v, depth):
  global answer
  visited[v] = 1
  if depth >= 4:
    answer = 1
    return
  for i in graph[v]:
    if visited[i] == 0:
      dfs(i, depth + 1)
      visited[i] = 0

answer = 0
visited = [0]*n
for i in range(n):
  dfs(i, 0)
  visited[i] = 0
  if answer == 1:
    break
print(answer)