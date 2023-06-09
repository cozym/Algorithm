# 1로 만들기
import sys
sys.setrecursionlimit(100000)
X = int(sys.stdin.readline())
dp = [0 for i in range(X+1)]

def make_one_dp(x):
    if x==1:
        return 0
    if dp[x]>0:
        return dp[x]
    dp[x] = make_one_dp(x-1)+1
    if x%2==0:
        t = make_one_dp(x//2)+1
        if dp[x]>t:
            dp[x] = t
    if x%3==0:
        t = make_one_dp(x//3)+1
        if dp[x]>t:
            dp[x] = t
    return dp[x]

res = make_one_dp(X)
print(res)