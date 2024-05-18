# 퇴사 2
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000000)

N = int(input())
coun = []
for _ in range(N):
    t,p = map(int,input().split())
    coun.append((t,p))
dp = [-1]*N

def recur(idx):
    if idx > N:
        return -1e9
    if idx == N:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    dp[idx] = max(recur(idx+1),recur(idx+coun[idx][0])+coun[idx][1])
    return dp[idx]

print(recur(0))