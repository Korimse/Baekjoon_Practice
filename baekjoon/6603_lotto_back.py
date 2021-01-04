##로또 백트래킹

def dfs(start, depth):
  if depth == 6:
    for i in range(6):
      print(visited[i], end = ' ')
    print()
    return
  
  for i in range(start, len(arr)):
    visited[depth] = arr[i]
    dfs(i+1, depth+1)

while True:
  arr = list(map(int, input().split()))
  if arr[0] == 0:
    break
  else:
    n = arr[0]
    del arr[0]
  visited = [0]*13

  dfs(0, 0)
  print()
