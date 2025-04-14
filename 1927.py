# 최소 힙
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

q = []

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(heappop(q) if q else 0)
    else:
        heappush(q,x)