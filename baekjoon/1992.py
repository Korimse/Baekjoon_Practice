import sys

input = sys.stdin.readline

n = int(input())
graph= []
for i in range(n):
  graph.append(list(input().strip()))

def cut(x, y, n):
  color = graph[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if color != graph[i][j]:
        print("(", end="")
        cut(x, y, n//2)
        cut(x, y+n//2, n//2)
        cut(x+n//2, y, n//2)
        cut(x+n//2, y+n//2, n//2)
        print(")", end="")
        return
  if color == '0':
    print('0', end="")
    return
  else:
    print('1', end="")
    return

cut(0, 0, n)
