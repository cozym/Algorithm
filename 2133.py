# 타일 채우기
import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(N+1)]

# dp[n] = dp[n-2]*3 (n이 2의 배수일 때)
# dp[i] = dp[n-4]*2 (n이 4의 배수일 때)
if N>=2:
    dp[2] = 3
if N>=4:
    dp[4] = dp[2]*3+2

for i in range(6,N+1,2):
    if i%2==0:
        dp[i] += dp[i-2]*3
        dp[i] += dp[i-4]*2

print(dp[N])
