# 꿀 아르바이트
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pay = list(map(int, input().split()))

ans = sum(pay[:m])
cur = ans

for i in range(n-m):
    cur -= pay[i]
    cur += pay[i+m]
    ans = max(ans, cur)

print(ans)