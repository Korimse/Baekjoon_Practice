n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*m for _ in range(n)]
answer = False
def dfs(x, y, cnt, sx, sy):
  global answer
  if answer == True:
    return
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m:
      if graph[nx][ny] == graph[x][y]:
        if visited[nx][ny] == 0:
          visited[nx][ny] = 1
          dfs(nx, ny, cnt+1, sx, sy)
          visited[nx][ny] = 0
        else:
          if cnt >= 4 and nx == sx and ny == sy:
            answer = True
            return
  return False

def solve(n, m):
  for i in range(n):
    for j in range(m):
      if not visited[i][j]:
        sx, sy = i, j
        visited[i][j] = 1
        dfs(i, j, 1, sx, sy)
      if answer:
        print("Yes")
        return
  print("No")
  return
solve(n, m)
