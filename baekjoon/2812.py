n, k = map(int, input().split())
num = list(input())
result, dk = [], k
for i in range(n):
  while dk > 0 and result:
    if result[-1] < num[i]:
      dk -= 1
      result.pop()
    else:
      break
  result.append(num[i])
print(''.join(result[:n-k]))