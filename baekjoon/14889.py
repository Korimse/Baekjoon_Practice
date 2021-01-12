n = int(input())

def dfs(i, cnt):
  global answer
  if cnt == n//2:
    start, link = 0, 0
    for i in range(n):
      for j in range(n):
        if select[i] and select[j]:
          start += arr[i][j]
        elif not select[i] and not select[j]:
          link += arr[i][j]
    answer = min(answer, abs(start-link))
  
  for j in range(i, n):
    if select[j]:
      continue
    select[j] = 1
    dfs(i+1, cnt+1)
    select[j] = 0


arr = [list(map(int, input().split())) for _ in range(n)]
select = [0 for _ in range(n)]
answer = 100000
dfs(0, 0)
print(answer)