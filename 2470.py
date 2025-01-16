# 두 용액
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
m = float('inf')
ans = []

arr.sort()

l, r = 0, N-1
while l < r:
    s = arr[l] + arr[r]
    if abs(s) < abs(m):
        m = s
        ans = [arr[l], arr[r]]
    if s < 0:
        l += 1
    elif s > 0:
        r -= 1
    else:
        break

print(*ans)