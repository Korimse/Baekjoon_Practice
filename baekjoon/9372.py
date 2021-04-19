from collections import deque

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    cnt = 0
    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        v = queue.popleft()
        
        for g in graph[v]:
            if visited[g] == False:
                visited[g] = True
                cnt += 1
                queue.append(g)
    print(cnt)