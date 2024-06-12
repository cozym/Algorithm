# 공룡게임
import sys
input = sys.stdin.readline

n = int(input())

dp = [([0]*3 for _ in range(3)) for _ in range(n)]
ndp = [([0]*2 for _ in range(2)) for _ in range(n)]

if n > 1:
    dp[1][0][0], dp[1][1][0], dp[1][2][0] = 1,1,1

for i in range(2,n+1):
    dp[i][0][0] = sum(dp[i-2])
    dp[i][0][1] = sum(dp[i-2])
    dp[i][0][2] = sum(dp[i-2])


# dp = [[0]*3 for _ in range(n+1)]
# ndp = [[0]*2 for _ in range(n+1)]

# dp[0][0], ndp[0][0] = 1,1

# if n > 1:
#     dp[1][0], dp[1][1], dp[1][2] = 1,1,1
#     ndp[1][0], ndp[1][1] = 1,1

# for i in range(2,n+1):
#     dp[i][0] = dp[i-2][0]*3 + dp[i-2][1]*3 + dp[i-2][2]*2
#     dp[i][1] = dp[i-2][0]*3 + dp[i-2][1] + dp[i-2][2]
#     dp[i][2] = dp[i-2][0]*2 + dp[i-2][1] + dp[i-2][2]
#     ndp[i][0] = ndp[i-2][0]*2 + ndp[i-2][1]*2
#     ndp[i][1] = ndp[i-2][0]*2 + ndp[i-2][1]

# print(dp[n][0]-ndp[n][0])