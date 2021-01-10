from collections import deque

n, t = map(int, input().split())
arr = deque()

for i in range(n):
  a, b = input().split()
  arr.append((a, b))
x, y = 0, 0
direct = 0
#right, up, left, down
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def direction():
  global direct
  if turn == 'left':
    direct += 1
  elif turn == 'right':
    direct -= 1
  if direct == -1:
    direct = 3
  elif direct == 4:
    direct = 0

move = 0
for i in range(n):
  a, turn = arr.popleft()
  pos = abs(int(a)- move)
  move = int(a)
  x = x + dx[direct]*pos
  y = y + dy[direct]*pos
  direction()

x = x + dx[direct]*(t-move)
y = y + dy[direct]*(t-move)
if n == 0:
  print(t, 0)
else:
  print(x, y)
