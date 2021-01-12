n = int(input())

def dfs(arr, cnt):
  if cnt == n:
    print(*arr)
    return

  for i in range(1, n+1):
    if i not in arr:
      arr.append(i)
      dfs(arr, cnt+1)
      arr.pop()

dfs([], 0)