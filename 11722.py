# 가장 긴 감소하는 부분 수열
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [1 for i in range(N)]

# dp[n] = max(dp[n-i])+1    (0<=1<n),(dp[n-i]+1 > dp[n])
