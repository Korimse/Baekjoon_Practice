from itertools import permutations

n = int(input())
arr = permutations(list(map(int, input().split())))
ans = 0
for k in arr:
  sum = 0
  for i in range(n-1):
    sum += abs(k[i]-k[i+1])
  ans = max(ans, sum)
print(ans)