n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(n+1):
    if i <= 1:
        dp[i] = 0
    elif i%6 == 0:
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
    elif i%3 == 0:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif i%2 == 0:
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[n])
