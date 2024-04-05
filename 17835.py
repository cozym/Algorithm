# 면접보는 승범이네
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
INF = int(1e11)

N,M,K = map(int,input().split())
R = [[] for _ in range(N+1)]
for _ in range(M):
    U,V,C = map(int,input().split())
    R[V].append((C,U))
interview = list(map(int,input().split()))
distance = [INF for _ in range(N+1)]
res = (0,0)

def dijkstra(start):
    distance[start] = 0
    Q = []
    heappush(Q,(0,i))

    while Q:
        nowCost, nowNode = heappop(Q)
        if distance[nowNode] < nowCost:
            continue
        for nextCost, nextNode in R[nowNode]:
            cost = nowCost+nextCost
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heappush(Q,(cost,nextNode))

for i in interview:
    dijkstra(i)  

distance[0] = -1

d = max(distance)
c = distance.index(d)
print(c)
print(d)