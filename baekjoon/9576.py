n = int(input())

for _ in range(n):
  m, k = map(int, input().split())
  book = [0]*(m+1)
  arr = []
  for i in range(k):
    arr.append(list(map(int, input().split())))
  
  arr.sort(key = lambda x : x[1])
  cnt = 0
  for a, b in arr:
    for i in range(a, b+1):
      if book[i] == 0:
        cnt += 1
        book[i] = 1
        break
  print(cnt)