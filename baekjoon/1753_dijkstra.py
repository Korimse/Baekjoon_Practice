import heapq
import sys
input = sys.stdin.readline

inf = 100000000
n, m = map(int, input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  d[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    for i in graph[now]:
      cost = dist + i[1]
      if cost < d[i[0]]:
        d[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

graph = [[] for _ in range(n+1)]
d = [inf]*(n+1)
start = int(input())
for i in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

dijkstra(start)
for i in d[1:]:
  if i == inf:
    print("INF")
  else:
    print(i)