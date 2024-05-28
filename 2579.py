# 계단 오르기
import sys
input =  sys.stdin.readline

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))
dp = [[0]*2 for _ in range(N+1)]

dp[1][0] = dp[1][1] = stairs[0]
# dp[n][0] = dp[n-1][1] / dp[n][1] = max(dp[n-2])
for i in range(2,N+1):
    dp[i][0] = dp[i-1][1] + stairs[i-1]
    dp[i][1] = max(dp[i-2]) + stairs[i-1]

print(max(dp[N]))