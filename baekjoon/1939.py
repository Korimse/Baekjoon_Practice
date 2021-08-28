from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
start = 10000000
end = 1
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    start = min(start, c)
    end = max(end, c)

f1, f2 = map(int, input().split())

def bfs(c):
    queue = deque()
    queue.append(f1)
    visited = [False]*(n+1)
    visited[f1] = True
    while queue:
        v = queue.popleft()
        for nv, nc in graph[v]:
            if not visited[nv] and nc >= c:
                visited[nv] = True
                queue.append(nv)
    return visited[f2]
result = start
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)