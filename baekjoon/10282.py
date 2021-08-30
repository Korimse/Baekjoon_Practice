import heapq
import sys
input = sys.stdin.readline

T = int(input())
INF = 1e9

for _ in range(T):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    count = 0
    maxv = -1
    for i in distance:
        if i != 1e9:
            count += 1
            if maxv < i:
                maxv = i
    print(count, maxv)