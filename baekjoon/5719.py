import heapq
from collections import deque

def bfs():
    q = deque()
    q.append(d)
    while q:
        now = q.popleft()
        if now == s:
            continue
        for prev, cost in reve[now]:
            if distance[now] == distance[prev]+cost:
                dropped[prev][now] = True
                q.append(prev)
def dijkstra():
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] and not dropped[now][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [1e9]*(n+1)
    dropped = [[False] * (n+1) for _ in range(n+1)]
    q = []
    reve = [[] for _ in range(n+1)]
    for i in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        reve[v].append((u, p))
    
    dijkstra()
    bfs()
    distance = [1e9]*(n+1)
    dijkstra()
    print(distance)
    if distance[d] != 1e9:
        print(distance[d])
    else:
        print(-1)