# 1,2,3 더하기 4
import sys
input = sys.stdin.readline

dp = [1] * 10001

for idx in range(2, 10001):
    dp[idx] += dp[idx-2]

for idx in range(3, 10001):
    dp[idx] += dp[idx-3]

for _ in range(int(input())):
    print(dp[int(input())])

# 1
# 11 , 2
# 111, 21, 3
# 1111, 211, 22, 31
# 11111, 2111, 221, 311, 23
# 111111, 21111, 2211, 3111, 231, 222
# 1111111, 211111, 22111, 31111, 2311, 