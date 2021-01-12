from collections import deque

n, m = map(int, input().split())

arr = list(map(int, input().split()))

queue = deque(arr)
b = [0]*n
count = 0
while queue:
  v = queue.popleft()
  maxv = 0
  swap = 0
  if v in b:
    continue
  if 0 in b:
    b[b.index(0)] = v
  else:
    for i in b:
      if i not in queue:
        swap = i
        break
      elif queue.index(i) > maxv:
        maxv = queue.index(i)
        swap = i
    b[b.index(swap)] = v
    count += 1

print(count)