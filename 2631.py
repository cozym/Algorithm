# 줄세우기
import sys
input = sys.stdin.readline

N = int(input())
child = []
for _ in range(N):
    child.append(int(input()))

dp = [1]*N

for i in range(N):
    for j in range(i):
        if child[i] > child[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1

print(N-max(dp))