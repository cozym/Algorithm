# 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
R = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]
Q = []
# M = int(input())
for _ in range(int(input())):
    s,d,c = map(int,input().split())
    R[s].append([c,d])

start, reach = map(int,input().split())

distance[start] = 0
heapq.heappush(Q,[0,start])
while Q:
    nowCost, nowNode = heapq.heappop(Q)

    if distance[nowNode] < nowCost:
        continue
    
    for node in R[nowNode]:
        nextCost, nextNode = node[0], node[1]
        if nowCost + nextCost < distance[nextNode]:
            distance[nextNode] = nowCost + nextCost
            heapq.heappush(Q,[nowCost + nextCost,nextNode])


print(distance[reach])