# 가장 큰 증가하는 부분 수열
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = A[:]
#dp[0] = A[0]

# dp[n] = max(dp[n-i]) + A[n] (0 <= i < n)
for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[j]+A[i] > dp[i]:
            dp[i] = dp[j]+A[i]
        
print(dp)