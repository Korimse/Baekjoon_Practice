from collections import deque

n, k = map(int, input().split())

INF = 100001
queue = deque()
queue.append(n)
visited = [0]*INF
moved = [0]*INF
while queue:
  num = queue.popleft()

  if num == k:
    print(visited[num])
    arr = []
    tmp = num
    for _ in range(visited[num] + 1):
      arr.append(tmp)
      tmp = moved[tmp]
    print(' '.join(map(str, arr[::-1])))
    break
  
  for i in (num+1, num-1, num*2):
    if 0<=i<INF and visited[i] == 0:
      visited[i] = visited[num] + 1
      moved[i] = num
      queue.append(i)
