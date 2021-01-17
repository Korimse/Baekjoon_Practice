import heapq
n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))

heapq.heapify(arr)
answer = 0
if len(arr) == 1:
  print(0)
else:
  while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    heapq.heappush(arr, a+b)
    answer += a + b
  print(answer)