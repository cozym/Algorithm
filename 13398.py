# 연속합 2
import sys

n = int(sys.stdin.readline())
S = list(map(int,sys.stdin.readline().split()))
dp = S[:] # 기본 버전
dp_r = S[:] # 하나씩 빼가며 저장하는 버전

# dp[n] = if dp[n-1] > 0: dp[n-1]+A[n] else: A[n]
for i in range(1,n):
    if dp[i] < dp[i-1]+S[i]:
        dp[i] = dp[i-1]+S[i]
    if dp_r[i] < dp_r[i-1]+S[i]:
        dp_r[i] = dp_r[i-1]+S[i]
    if dp[i-2] > dp_r[i-1] and dp_r[i-2]+S[i] > dp_r[i]:
        dp_r[i-2] = dp[i-2]
        dp_r[i] = dp[i-2]+S[i]

print(max(dp_r))