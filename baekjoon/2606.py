from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque()
    queue.append(1)
    visited = [0] * (n+1)
    visited[1] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
    return visited.count(1)-1
print(bfs())