n = int(input())
graph=[[] for _ in range(n+1)]
for i in range(1, n+1):
  graph[i].append(int(input()))
result = []
def dfs(s, g):
  visited[s] = 1
  for i in graph[s]:
    if visited[i] == 0:
      dfs(i, g)
    elif visited[i] and i==g:
      result.append(i)

for i in range(1, n+1):
  visited = [0]*(n+1)
  dfs(i, i)
print(len(result))
for i in result:
  print(i)
