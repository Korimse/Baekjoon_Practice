
def fibo(n):
    if dp[n-1] == -1:
        dp[n-1] = fibo(n-1)
    
    return dp[n-1] + dp[n-2]

n = int(input())
dp = [-1]*(n+1)

dp[0] = 0
dp[1] = 1

print(fibo(n))