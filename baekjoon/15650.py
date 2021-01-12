n, m = map(int, input().split())

def dfs(arr, count, idx):
  if count == m:
    print(arr)
    return
  
  for i in range(idx, n+1):
    if d[i] == 1:
      continue
    d[i] = 1
    arr.append(i)
    dfs(arr, count+1, idx+1)
    arr.pop()
    for j in range(i+1, n+1):
      d[j] = 0

lis = []
d = [0]*(n+1)
dfs([], 0, 1)
