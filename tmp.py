import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] * (v+1) for _ in range(v+1)]
distance = [11] * (v+1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


dijkstra(start)
print(distance)

for i in range(1, v+1):
    if distance[i] == 11:
        print("INF")
        continue
    print(distance[i])