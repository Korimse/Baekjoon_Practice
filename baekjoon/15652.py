n, m = map(int, input().split())

def dfs(arr, cnt, idx):
  if cnt == m:
    print(*arr)
    return
  
  for i in range(idx, n+1):
    arr.append(i)
    dfs(arr, cnt+1, i)
    arr.pop()

dfs([], 0, 1)