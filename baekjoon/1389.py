import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    distance = [9999]*(n+1)
    q = []
    heapq.heappush(q, (start, 0))
    distance[0] = 0
    distance[start] = 0

    while q:
        v, d = heapq.heappop(q)
        
        for nv, nd in graph[v]:
            cost = d + nd
            if cost < distance[nv]:
                distance[nv] = cost
                heapq.heappush(q, (nv, cost))
    return distance
answer = []
for i in range(1, n+1):
    answer.append(sum(dijkstra(i)))
print(answer.index(min(answer))+1)