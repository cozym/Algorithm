# 보석 도둑
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, K = map(int, input().split())
J = []
C = []
for _ in range(N):
    m, v = map(int, input().split())
    J.append([m, v])
for _ in range(K):
    C.append(int(input()))

C.sort()
J.sort(reverse=True)
hq = []
ans = 0
# 수용무게가 낮은 가방부터, 넣을 수 있는 보석 중에, 가장 비싼거로
for bag in C:
    while J:
        weight, cost = J.pop()  # 가벼운 보석부터 꺼내서
        if bag >= weight:    # 가방에 들어가면 우선순위큐
            heappush(hq, -cost)
        else:
            J.append([weight, cost])
            break
    if hq:  # 넣을 수 있는 보석중에 가장 비싼거로
        ans -= heappop(hq)

print(ans)