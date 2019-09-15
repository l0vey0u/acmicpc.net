T = int(input())
p = []
dp = [0 for _ in range(T+1)]
for _ in range(T):
    p.append(int(input()))
for n in range(1, T+1):
    dp[n] = max(dp[n-2], dp[n-1]) + p[n-1]
print(dp[T]) 
