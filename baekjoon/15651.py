n, m = map(int, input().split())

def dfs(arr, count):
  if count == m:
    print(*arr)
    return

  for i in range(1, n+1):
    arr.append(i)
    dfs(arr, count+1)
    arr.pop()
dfs([], 0)