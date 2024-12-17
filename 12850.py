# 본대 산책2
import sys
input = sys.stdin.readline

D = int(input())
MOD = 1000000007
N = 8
dp = {}

dp[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]

def daq(d, s, e):
    if d <= 1:
        return dp[d][s][e]
    
    dp.setdefault(d, [[0 for _ in range(N)] for _ in range(N)])
    if dp[d][s][e]:
        return dp[d][s][e]
    
    half1 = d // 2
    half2 = d // 2 + 1 if d % 2 != 0 else d // 2

    for m in range(N):
        dp[d][s][e] += daq(half1, s, m) * daq(half2, m, e)
        dp[d][s][e] %= MOD

    return dp[d][s][e]

print(daq(D, 0, 0))