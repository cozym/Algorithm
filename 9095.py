# 1,2,3 더하기
import sys

T = int(sys.stdin.readline())
L = []
for i in range(T):
    L.append(int(sys.stdin.readline()))

# if max(L)<3:
#     dp = [range(3)]
# else:
#     dp = [0 for i in range(max(L))]
dp = [0 for i in range(11)] 
dp[0] = 1
dp[1] = 2
dp[2] = 4

for j in range(3,max(L)):
    dp[j] = dp[j-3]+dp[j-2]+dp[j-1]
for k in L:
    print(dp[k-1])