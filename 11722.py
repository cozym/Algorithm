# 가장 긴 감소하는 부분 수열
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [1 for i in range(N)]

# dp[n] = max(dp[n-i])+1    (0<=i<n),(A[n-i]+1 > A[n])
for i in range(N):
    for j in range(i):
        if dp[i] < dp[j]+1 and A[j] > A[i]:
            dp[i] = dp[j]+1

print(max(dp))