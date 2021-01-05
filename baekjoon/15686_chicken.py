import itertools
n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
chicken = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      chicken.append((i, j))
      graph[i][j] = 0

com = list(itertools.combinations(chicken, m))
answer = 100000
for i in range(len(com)):
  distance = 0
  for j in range(n):
    for k in range(n):
      if graph[j][k] == 1:
        tmp = 100000
        for l in range(m):
          tmp = min(tmp, abs(com[i][l][0]-j) + abs(com[i][l][1]-k))
        distance += tmp
  answer = min(distance, answer)
print(answer)