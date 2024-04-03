# 민준이와 마산 그리고 건우
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
INF = int(1e9)

V,E,P = map(int,input().split())
R = [[] for _ in range(V+1)]

def dijkstra(start):
    distance = [INF for _ in range(V+1)]
    distance[start] = 0
    Q = []
    heappush(Q,[0,start])

    while Q:
        nowCost, nowNode = heappop(Q)
        if distance[nowNode] < nowCost:
            continue
        for nextCost,nextNode in R[nowNode]:
            if nowCost+nextCost < distance[nextNode]:
                distance[nextNode] = nowCost+nextCost
                heappush(Q,[nowCost+nextCost,nextNode])
    
    return distance

for _ in range(E):
    a,b,c = map(int,input().split())
    R[a].append([c,b])
    R[b].append([c,a])

distanceFrom1 = dijkstra(1)
distanceFromP = dijkstra(P)

if distanceFromP[1]+distanceFromP[V] <= distanceFrom1[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")