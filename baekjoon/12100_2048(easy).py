import sys, copy

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def move_up(a):
  for j in range(n):
    idx = 0
    for i in range(1, n):
      if a[i][j]:
        temp = a[i][j]
        a[i][j] = 0
        if a[idx][j] == 0:
          a[idx][j] = temp
        elif a[idx][j] == temp:
          a[idx][j] = temp * 2
          idx += 1
        else:
          idx += 1
          a[idx][j] = temp
  return a

def move_down(a):
  for j in range(n):
    idx = n-1
    for i in range(n - 2, -1, -1):
      if a[i][j]:
        temp = a[i][j]
        a[i][j] = 0
        if a[idx][j] == 0:
          a[idx][j] = temp
        elif a[idx][j] == temp:
          a[idx][j] = temp * 2
          idx -= 1
        else:
          idx -= 1
          a[idx][j] = temp
  return a

def move_left(a):
  for i in range(n):
    idx = 0
    for j in range(1, n):
      if a[i][j]:
        temp = a[i][j]
        a[i][j] = 0
        if a[i][idx] == 0:
          a[i][idx] = temp
        elif a[i][idx] == temp:
          a[i][idx] = temp * 2
          idx += 1
        else:
          idx += 1
          a[i][idx] = temp
  return a

def move_right(a):
  for i in range(n):
    idx = n-1
    for j in range(n - 2, -1, -1):
      if a[i][j]:
        temp = a[i][j]
        a[i][j] = 0
        if a[i][idx] == 0:
          a[i][idx] = temp
        elif a[i][idx] == temp:
          a[i][idx] = temp * 2
          idx -= 1
        else:
          idx -= 1
          a[i][idx] = temp
  return a

def dfs(a, k):
  global maxv
  if k == 5:
    for i in range(n):
      for j in range(n):
        if maxv < a[i][j]: maxv = a[i][j]
    return
  dfs(move_left(copy.deepcopy(a)), k+1)
  dfs(move_right(copy.deepcopy(a)), k+1)
  dfs(move_up(copy.deepcopy(a)), k+1)
  dfs(move_down(copy.deepcopy(a)), k+1)


maxv = 0
dfs(a, 0)
print(maxv)
