# 상자 넣기
import sys
input = sys.stdin.readline

n = int(input())
sizes = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if sizes[j] < sizes[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))