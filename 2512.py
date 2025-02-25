# 예산
import sys
input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
budget = int(input())

requests.sort()
l,r = 1, max(requests)
ans = 0

while l <= r:
    m = (l + r) // 2
    total = 0

    for r in requests:
        total += min(r, m)

    if total <= budget:
        l = m + 1
        ans = m
    else:
        r = m - 1

print(ans)