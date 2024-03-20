# 1,2,3 더하기 5
import sys

dp = [[0,0,0] for i in range(100001)]
dp[0] = [1,0,0]
dp[1] = [0,1,0]
dp[2] = [1,1,1]

for i in range(3,100001):
    dp[i][0] = dp[i-1][1]+dp[i-1][2]%1000000009
    dp[i][1] = dp[i-2][0]+dp[i-2][2]%1000000009
    dp[i][2] = dp[i-3][0]+dp[i-3][1]%1000000009

T = int(sys.stdin.readline().rstrip())

for j in range(T):
    n = int(sys.stdin.readline().rstrip())
    if n==0:
        print(0)
    else:
        print(sum(dp[n-1])%1000000009)