import sys
input = sys.stdin.readline
k = int(input())
for _ in range(k):
  n = int(input())
  arr = []
  for i in range(n):
    arr.append(list(map(int, input().split())))
  arr.sort()
  cnt = 1
  min = arr[0][1]
  for i in range(n):
    if arr[i][1] < min:
      cnt += 1
      min = arr[i][1]
  print(cnt)