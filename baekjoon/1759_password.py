n, m = map(int, input().split())

s = list(input().split())
d = []
answer = []
visited = [False]*(m)
s.sort()
def select(cnt, idx):
  if cnt == n:
    answer.append(''.join(map(str, d)))
    return
  
  for i in range(idx, m):
    if visited[i] == False:
      d.append(s[i])
      visited[i] = True
      select(cnt+1, i+1)
    else:
      continue
    visited[i] = False
    d.pop()

select(0, 0)
for i in answer:
  mo = 0
  ja = 0
  for j in i:
    if j in 'aeiou':
      mo += 1
    else:
      ja += 1
  if mo >= 1 and ja >= 2:
    print(i)