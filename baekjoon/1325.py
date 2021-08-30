from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited = [0] * (n+1)
    visited[x] = 1
    while q:
        nx = q.popleft()
        for i in graph[nx]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return visited.count(1)-1

result = []
maxv = -1
for i in range(1, n+1):
    count = bfs(i)
    if count > maxv:
        maxv = count
        result = [i]
    elif count == maxv:
        result.append(i)

for i in result:
    print(i, end = ' ')
