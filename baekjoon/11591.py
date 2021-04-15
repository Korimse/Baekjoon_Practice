n, q = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

def dijkstra(start, k):
  visited = [0]*(n+1)
  need_visit = [[start, 1000000]]

  while need_visit:
    current_destination, usado = need_visit.pop()
    if visited[current_destination] == 0 and usado >= k:
      visited[current_destination] = 1
      need_visit.extend(graph[current_destination])
  count = visited.count(True)
  return count-1

answer = []

for i in range(q):
  a, b = map(int, input().split())
  answer.append(dijkstra(b, a))

print('\n'.join(map(str, answer)))