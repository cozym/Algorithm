# RGB 거리
import sys

N = int(sys.stdin.readline())

dp = [[0,0,0] for i in range(N)]
RGB = []
RGB.append(list(map(int,sys.stdin.readline().split())))
dp[0] = RGB[0].copy()

# 점화식 dp[i][r] = min(dp[i-1][g]+rgb[i][r] , dp[i-1][b]+rgb[i][r])
for i in range(1,N):
    RGB.append(list(map(int,sys.stdin.readline().split())))
    dp[i][0] = min(dp[i-1][1]+RGB[i][0], dp[i-1][2]+RGB[i][0])
    dp[i][1] = min(dp[i-1][0]+RGB[i][1], dp[i-1][2]+RGB[i][1])
    dp[i][2] = min(dp[i-1][0]+RGB[i][2], dp[i-1][1]+RGB[i][2])

print(min(dp[N-1]))