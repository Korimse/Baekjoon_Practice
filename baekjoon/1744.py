n = int(input())
ys = []
ms = []
zo = []
for i in range(n):
  v = int(input())
  if v > 1:
    ys.append(v)
  elif v < 0:
    ms.append(v)
  else:
    zo.append(v)

ys.sort(reverse= True)
ms.sort()
answer = 0

if len(ys)%2 == 0:
  for i in range(0, len(ys)-1, 2):
    answer += ys[i] * ys[i+1]
if len(ys)%2 != 0:
  for i in range(0, len(ys)-1, 2):
    answer += ys[i] * ys[i+1]
  answer += ys[-1]

if len(ms)%2 == 0:
  for i in range(0, len(ms)-1, 2):
    answer += ms[i] * ms[i+1]
if len(ms)%2 != 0:
  for i in range(0, len(ms)-1, 2):
    answer += ms[i] * ms[i+1]
  if 0 not in zo:
    answer += ms[-1]
answer += sum(zo)
print(answer)