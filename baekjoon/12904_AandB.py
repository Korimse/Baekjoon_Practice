s = list(input())
t = list(input())

while True:
  if len(t) == len(s):
    if t == s:
      print(1)
    else:
      print(0)
    break
  l = t.pop()
  if l == 'B':
    t = t[::-1]