# 합분해
import sys

N,K = map(int,sys.stdin.readline().split())
dp = [[0 for i in range(K+1)] for i in range(N+1)]

# dp[n][k] = sum(dp[n-j][k-1])  0<=j<=n
for k in range(1,K+1):
    for n in range(N+1):
        if k==1:
            dp[n][k] = 1
        for i in range(n+1):
            dp[n][k] = (dp[n][k]+dp[i][k-1])%1000000000

print(dp[n][k])