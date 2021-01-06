from collections import deque
INF = int(1e9)
f, s, g, u, d = map(int, input().split())
dire = [u, -d]
arr = [0]*f

visited = [False]*f
d = [-1]*(f)

queue = deque()
queue.append(s-1)
visited[s-1] = True
d[s-1] = 0
while queue:
  v = queue.popleft()

  for i in range(2):
    n = v+dire[i]
    if 0<=n<f and visited[n] == False:
      queue.append(n)
      d[n] = d[v] + 1
      visited[n] = True

if -1 in d:
  print("use the stairs")
else:
  print(d[g-1])