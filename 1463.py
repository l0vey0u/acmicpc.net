dp = {1:0,2:1,3:1}
def r(n):
    if n%3 == 0:
        if n%2 == 0:
            dp[n] = 1 + min(r(n//3), r(n//2), r(n-1))
        else:
            dp[n] = 1 + min(r(n//3), r(n-1))
    elif n%2 == 0:
        dp[n] = 1 + min(r(n//2), r(n-1))
    elif n > 1:
        dp[n] = 1 + r(n-1)
    return dp[n]
n = int(input())
print(r(n))
