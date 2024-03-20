# 연속합 2
import sys

n = int(sys.stdin.readline())
S = list(map(int,sys.stdin.readline().split()))
dp = S[:] # 기본 버전
dp_r = S[:] # 하나씩 빼가며 저장하는 버전
M = S[0] # max값 저장

# dp[n] = if dp[n-1] > 0: dp[n-1]+A[n] else: A[n]
for i in range(1,n):
    if dp[i] < dp[i-1]+S[i]:
        dp[i] = dp[i-1]+S[i]
    dp_r[i] = max(dp[i-1],dp_r[i-1]+S[i])
    
print(max(max(dp),max(dp_r)))