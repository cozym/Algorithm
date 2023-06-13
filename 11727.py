# 2*n 타일링 2
import sys

n = int(sys.stdin.readline())

dp = [0 for i in range(n+1)]
dp[0] = 1
dp[1] = 3

if n<3:
    print(dp[n-1])
else:
    for i in range(2,n+1):
        dp[i] = dp[i-2]*2+dp[i-1]
    print(dp[n-1]%10007)