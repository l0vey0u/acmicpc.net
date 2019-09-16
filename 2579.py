T = int(input())
scr = []
for _ in range(T):
    scr.append(int(input()))
dp = [ 0 for _ in range(T+1) ]
for n in range(1, T+1):
    dp[n] = scr[n-1]
    if n == 1:
        continue
    if n == 2:
        if T != 3:
            dp[n] += scr[n-2]
            continue
    if scr[n-2] > scr[n-3]:
        dp[n] += dp[n-1]
    else:
        dp[n] += dp[n-2]
print(dp[T])
