from collections import deque

n, m = map(int, input().split())

arr = [i for i in range(101)]
for i in range(n+m):
  a, b = map(int, input().split())
  arr[a] = b
visited = [0]*101
queue = deque()
queue.append(1)
while queue:
  v = queue.popleft()
  for i in range(1, 7):
    x = v+i
    if x > 100:
      continue
    x = arr[x]
    if visited[x] == 0 or visited[x] > visited[v]+1:
      visited[x] = visited[v] + 1
      queue.append(x)
print(visited[-1])
