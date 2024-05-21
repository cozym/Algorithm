# 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
bag = []
for _ in range(N):
    w,v = map(int,input().split())
    bag.append((w,v))

dp = [[-1]*100001 for _ in range(N)]

def recur(idx, weight):
    if weight > K:
        return -10000000000
    if idx == N:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    dp[idx][weight] = max(recur(idx+1, weight), recur(idx+1, weight+bag[idx][0])+bag[idx][1])
    return dp[idx][weight]

print(recur(0,0))