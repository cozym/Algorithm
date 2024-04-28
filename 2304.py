# 창고 다각형
import sys
input = sys.stdin.readline

N = int(input())
storage = [0 for _ in range(1001)]
tall = 0
for _ in range(N):
    L,H = map(int,input().split())
    storage[L] = H
    if tall < H:
        tall = H
        point = L

print()
# storage.sort()

# currentH = 0
# for l,h in storage:
#     if currentH < h:
        