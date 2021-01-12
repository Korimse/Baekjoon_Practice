s = list(input()[:-1])
s2 = list()
n = int(input())
for _ in range(n):
  c = input()
  if c[0] == 'L' and s:
    s2.append(s.pop())
  elif c[0] == 'D' and s2:
    s.append(s2.pop())
  elif c[0] == 'B' and s:
    s.pop()
  elif c[0] == 'P':
    s.append(c[2])
s2 = s2[::-1]
print(''.join(s+s2))