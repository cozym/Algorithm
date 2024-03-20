# 제곱수의 합
import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(N+1)]

# dp[i] = min(dp[i-j**2])+1
for i in range(N+1):
    dp[i] = i
    for j in range(int(i**0.5)+1):
        if dp[i] > dp[i-j**2]+1:
            dp[i] = dp[i-j**2]+1

print(dp[N])