# 군탈체포조
import sys
from itertools import permutations
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)
nx = [0,1,0,-1]
ny = [-1,0,1,0]

N = int(input())
costMap = []
deserters = []  # 탈영병 위치
distances = {} # 탈영병의 위치로부터 최단거리들
ans = INF

for y in range(N):
    line = list(map(int,input().split()))
    for x in range(N):
        if line[x] == -1:   # 부대 위치 저장
            home = (y,x)
        elif line[x] == 0:  # 탈영병 위치 저장
            deserters.append((y,x))
    costMap.append(line)

costMap[home[0]][home[1]] = 0   # 부대 cost 0으로 변경

# 시작 위치를 기준으로 최단거리 맵 반환
def dijkstra(start):
    sy,sx = start
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[sy][sx] = 0
    Q = []
    heappush(Q,[0,start])

    while Q:
        nowCost, nowNode = heappop(Q)
        y,x = nowNode
        if distance[y][x] < nowCost:
            continue
        for idx in range(4):
            nextX = x + nx[idx]
            nextY = y + ny[idx]
            if 0 <= nextX and nextX < N and 0 <= nextY and nextY < N:
                if nowCost+costMap[nextY][nextX] < distance[nextY][nextX]:
                    distance[nextY][nextX] = nowCost+costMap[nextY][nextX]
                    heappush(Q,[nowCost+costMap[nextY][nextX],(nextY,nextX)])
    return distance

distances[home] = dijkstra(home)    # 부대에서부터의 최단거리
for node in deserters:
    distances[node] = dijkstra(node)    # 각 탈영병으로부터의 최단거리

per = permutations(deserters,len(deserters))    # 탈영병 위치를 순열로 모든 경우를 저장

for course in list(per):
    groupCost = 0
    current = home  # 시작 위치는 부대
    for node in course:
        y,x = node
        groupCost += (distances[current])[y][x] # 탈영병 위치로 이동 및 이동비용++
        current = node  # 이동한 탈영병 위치로 기준 변경
    y,x = home
    groupCost += (distances[current])[y][x] # 마지막 탈영병 위치에서 부대 북귀 비용++
    if groupCost < ans:
        ans = groupCost

print(ans)