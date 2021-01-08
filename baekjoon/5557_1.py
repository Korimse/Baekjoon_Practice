import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
arr = list(map(int, input().split()))

d = []
def dfs(su, cnt, idx):
  if cnt == n-2:
    d.append(su)
    return
  a = su + arr[idx]
  if 0<=a<=20:
    dfs(a, cnt+1, idx+1)

  b = su - arr[idx]
  if 0<=b<=20:
    dfs(b, cnt+1, idx+1)

dfs(arr[0], 0, 1)
print(Counter(d))
##백트래킹 시간초과뜸!

import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
dp = [[0] * 21 for i in range(n)]
dp[0][s[0]] = 1
for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if 0 <= j + s[i] <= 20: dp[i][j + s[i]] += dp[i - 1][j]
            if 0 <= j - s[i] <= 20: dp[i][j - s[i]] += dp[i - 1][j]
print(dp[n - 2][s[-1]])