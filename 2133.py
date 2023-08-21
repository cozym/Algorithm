# 타일 채우기
import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(N+1)]

if N>=2:    # N이 2인 경우
    dp[2] = 3
if N>=4:    # N이 4인 경우
    dp[4] = dp[2]*3+2

for i in range(6,N+1):
    if i%2==0:  # 홀수는 모두 0
        dp[i] += dp[i-2]*3  # dp[2]를 dp[n-2]에 곱하여 더해줌
        for j in range(i-4,-1,-2):  # i-4부터 2씩 감소하며 특수패턴 2가지를 곱하여 더해줌
            dp[i] += dp[j]*2
        dp[i]+=2 # dp[2] 패턴이 없는 특수한 패턴 2가지 더해줌

print(dp[N])