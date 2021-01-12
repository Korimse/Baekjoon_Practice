n, m, k = map(int, input().split())
store = [0] + list(map(int, input().split())) + [k]

store.sort()

left = 1
right = k-1
mid = 0
while left <= right:
  mid = int((left+right)/2)
  ns = 0
  for i in range(1, len(store)):
    dist = store[i] - store[i-1]
    ns += int(dist/mid)
    if (dist%mid) == 0:
      ns -= 1
  
  if ns > m:
    left = mid + 1
  else:
    right = mid -1

print(left)