# 이친수
import sys

dp = [[0,0] for i in range(90)]
dp[0] = [0,1]

for n in range(1,90):
    dp[n][0] = sum(dp[n-1])
    dp[n][1] = dp[n-1][0]

N = int(sys.stdin.readline())
print(sum(dp[N-1]))