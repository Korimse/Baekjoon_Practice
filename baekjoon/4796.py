import sys
input = sys.stdin.readline
i = 1
while True:
  a, b, c = map(int, input().split())
  if a == b == c == 0:
    break
  cnt = 0
  t = (c//b)*a
  t += min((c%b), a)
  print('Case %d: %d' %(i, t))
  i+=1