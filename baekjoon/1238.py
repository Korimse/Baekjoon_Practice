import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
graph_b = [[] for _ in range(n+1)]
for i in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph_b[b].append((a, c))

def dijkstra(start, graph):
  q = []
  distance = [99999]*(n+1)
  heapq.heappush(q, (start, 0))
  distance[start] = 0
  while q:
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist+i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (i[0], cost))
  return distance

go = dijkstra(x, graph)
back = dijkstra(x, graph_b)
answer = 0
for i in range(1, n+1):
  answer = max(answer, go[i]+back[i])
print(answer) 
