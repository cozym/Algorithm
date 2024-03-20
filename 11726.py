# 2*n 타일링
import sys

n = int(sys.stdin.readline())
dp = [1,2]
if n<3:
    print(dp[n-1])
else:
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    print(dp[n-1]%10007)