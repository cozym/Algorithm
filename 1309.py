# 동물원
import sys

H = int(sys.stdin.readline())
# dp[n][x] = dp[n-1][y] ( y는 x를 제외한 부분, 0일때는 모두 포함 )
# x=0 : 노배치 , x=1 : 왼쪽배치 , x=2 : 오른쪽배치
dp = [[1,1,1] if i==0 else [0,0,0] for i in range(H)]

for n in range(1,H):
    dp[n][0] = sum(dp[n-1]) % 9901
    dp[n][1] = dp[n-1][0] + dp[n-1][2] % 9901
    dp[n][2] = dp[n-1][0] + dp[n-1][1] % 9901

print(sum(dp[H-1])%9901)