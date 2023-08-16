# 가장 긴 바이토닉 부분 수열
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1 for i in range(N)]
dp_r = [1 for i in range(N)]
bitonic = [0 for i in range(N)]

# dp[n] = max(dp[n-i])+1 (0 <= i < n)
for i in range(N):
    for j in range(i):
        if dp[i] < dp[j]+1 and A[i] > A[j]:
            dp[i] = dp[j]+1
        if dp_r[N-i-1] < dp_r[N-j-1]+1 and A[N-i-1] > A[N-j-1]:
            dp_r[N-i-1] = dp_r[N-j-1]+1

# dp[k] = LIS(dp[k])+LDS(dp[k])-1
for k in range(N):
    bitonic[k] = dp[k]+dp_r[k]-1
    
print(max(bitonic))