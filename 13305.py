# 주유소
import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
now = cost[0]
ans = 0

for i in range(N-1):
    if cost[i] < now:
        now = cost[i]
    ans += now * road[i]

print(ans)