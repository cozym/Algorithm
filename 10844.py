# 쉬운 계단 수
import sys

dp = [[0]*10 for i in range(100)]
dp[0] = [0,1,1,1,1,1,1,1,1,1]

# 0,9로 끝나는 수만 따로 처리 / 1~8로 끝나는 수는 (i-1),(i+1)로 계단수 생성 가능
for n in range(1,100):
    dp[n][0] = dp[n-1][1] % 1000000000
    for i in range(1,9):
        dp[n][i] = (dp[n-1][i-1]+dp[n-1][i+1]) % 1000000000
    dp[n][9] = dp[n-1][8] % 1000000000

N = int(sys.stdin.readline())
print(sum(dp[N-1])%1000000000)