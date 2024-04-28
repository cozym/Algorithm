# 창고 다각형
import sys
input = sys.stdin.readline

N = int(input())
storage = [0 for _ in range(1001)]
res = 0

for _ in range(N):
    L,H = map(int,input().split())
    storage[L] = H

m = max(storage)
tallPoint = storage.index(m)

currentH = 0
for l in range(tallPoint):
    currentH = max(currentH,storage[l])
    res += currentH

currentH = 0
for r in range(1000,tallPoint,-1):
    currentH = max(currentH,storage[r])
    res += currentH

res += m
print(res)