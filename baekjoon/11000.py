import heapq
import sys
input= sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
cnt = 0
q = []
arr.sort()
for i in arr:
  if len(q) != 0 and q[0] <= i[0]:
    heapq.heappop(q)
  heapq.heappush(q, i[1])

print(len(q))