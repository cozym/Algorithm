# 오르막 수
import sys

N = int(sys.stdin.readline())
dp = [[1 for i in range(10)] if j==0 else [0 for i in range(10)] for j in range(N)]

# dp[n][x] = sum(dp[n-1][y]) (0 <= y <= x)
for n in range(1,N):
    for x in range(10):
        dp[n][x] = sum(dp[n-1][0:x+1])%10007

print(sum(dp[N-1])%10007)