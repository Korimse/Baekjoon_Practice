n = int(input())
dp = [0] * (n + 1)
arr = [0]
tmp = list(map(int, input().split()))
for t in tmp:
  arr.append(t)
dp[1] = arr[1]
dp[2] = max(arr[1]*2, arr[2])
for i in range(3, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i-j]+arr[j])
print(dp[n])