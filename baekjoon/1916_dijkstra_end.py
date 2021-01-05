import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (start, 0))
  distance[start] = 0
  while q:
    now, dist = heapq.heappop(q)
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (i[0], cost))

dijkstra(start)
print(distance[end])