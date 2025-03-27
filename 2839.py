# 설탕 배달
import sys
input = sys.stdin.readline

n = int(input())
ans = -1
for five in range(0, n+1, 5):
    if (n-five) % 3 == 0:
        ans = ((n-five) // 3) + (five // 5)

print(ans)