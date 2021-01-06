n = list(input())
m = list(input())
result = [["" for _ in range(len(m)+1)]for _ in range(len(n)+1)]

for i in range(1, len(n)+1):
    for j in range(1, len(m)+1):
      if n[i-1] == m[j-1]:
        result[i][j] = result[i-1][j-1] + n[i-1]
      else:
        if len(result[i-1][j]) > len(result[i][j-1]):
          result[i][j] = result[i-1][j]
        else:
          result[i][j] = result[i][j-1]

if len(result[-1][-1]) == 0:
  print(0)
else:
  print(len(result[-1][-1]))
  print(result[-1][-1])
