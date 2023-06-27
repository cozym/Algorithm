# 가장 긴 증가하는 부분 수열
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [1 for i in range(N)]

# dp[i] = A[i]로 끝나는 LIS
# if A[j]<A[i]: dp[i] = max(dp[j])+1
for i in range(N):
    for j in range(i):
        if A[j]<A[i] and dp[j]+1>dp[i]:
            dp[i]=dp[j]+1

print(max(dp))
