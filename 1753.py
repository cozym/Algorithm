# 최단경로
import sys
from heapq import heappush,heappop
INF = int(1e9)
input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())
distance = [INF for _ in range(V+1)]
R = [[] for _ in range(V+1)]

for idx in range(E):
    u,v,w = map(int,input().split())
    R[u].append((w,v))

def dijkstra(start):
    q = []
    heappush(q,(0,start))
    distance[start] = 0

    while q:
        nowCost, nowNode = heappop(q)
        if distance[nowNode] < nowCost: # 저장된 거리가 이미 짧은 경우 스킵
            continue
        for nextCost, nextNode in R[nowNode]:
            if nowCost+nextCost < distance[nextNode]:   # 현재 노드까지 거리 + 다음 노드까지의 거리가 저장된 거리보다 짧으면 업데이트
                distance[nextNode] = nowCost+nextCost
                heappush(q,(nowCost+nextCost,nextNode)) # 업데이트 시 큐에 넣어서 다음 최단거리 비교탐색

dijkstra(K)

for d in range(1,V+1):
    if distance[d]==INF:
        print("INF")
    else:
        print(distance[d])