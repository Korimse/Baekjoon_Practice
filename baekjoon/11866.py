import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
result = []
arr = deque(arr)
cur = 0
while len(result) < n:
  for i in range(m-1):
    t = arr.popleft()
    arr.append(t)
  result.append(arr.popleft())

print("<", end='')
print(', '.join(map(str, result)) + ">")
