import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
for i in range(n):
  k = int(input())

  if k == 0:
    if h:
      v = -heapq.heappop(h)
      print(v)
    else:
      print(0)
  else:
    heapq.heappush(h, -k)
