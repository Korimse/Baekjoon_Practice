import heapq

n, k = map(int, input().split())
ju = []
for i in range(n):
  a, b = map(int, input().split())
  heapq.heappush(ju, (a, b))
bag = []
for i in range(k):
  s = int(input())
  heapq.heappush(bag, s)

result = 0
small = []

for _ in range(k):
  s = heapq.heappop(bag)

  while ju and s >= ju[0][0]:
    w, v = heapq.heappop(ju)
    heapq.heappush(small, -v)
  
  if small:
    result -= heapq.heappop(small)
  elif not ju:
    break

print(result)