n, l = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
cnt = 1
tape = arr[0]
for i in range(1, n):
  if arr[i] >= tape + l:
    cnt += 1
    tape = arr[i]
  else:
    continue
print(cnt)