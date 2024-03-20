# 연속합
import sys

n = int(sys.stdin.readline())
dp = list(map(int,sys.stdin.readline().split()))  # dp[i] = arr[i]를 끝으로 하는 연속합

for i in range(1,n):
    if dp[i-1]>0:
        dp[i] += dp[i-1]

print(max(dp))