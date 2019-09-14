T = input()
pTbl = []
for _ in range(T):
    pTbl.append(map(int, raw_input().split()))
dp = [ [0,0,0] for _ in range(T+1) ]
dp[1] = pTbl[0]
for n in range(2,T+1):
    dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + pTbl[n-1][0]
    dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + pTbl[n-1][1]
    dp[n][2] = min(dp[n-1][1], dp[n-1][0]) + pTbl[n-1][2]
print(sorted(dp[T])[0])
