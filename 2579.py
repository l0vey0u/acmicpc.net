T = int(input())
p = []
for _ in range(T):
    p.append(int(input()))
dp = [ 0 for _ in range(T+1) ]
dp[1] = p[0]
dp[2] = p[0] + p[1]
dp[3] = max(p[0], p[1]) + p[2]
for n in range(3, T+1):
    dp[n] = max(dp[n-3] + p[n-2] + p[n-1], dp[n-2] + p[n-1])
print(dp[T])
