# 녹색 옷 입은 애가 젤다지?
import sys
from heapq import heappush,heappop
INF = int(1e9)
input = sys.stdin.readline
nX = [0,1,0,-1]
nY = [-1,0,1,0]

def dijkstra(n):
    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = cave[0][0]
    q = []
    heappush(q,[cave[0][0],(0,0)])

    while q:
        nowCost,nowPosition = heappop(q)
        x,y = nowPosition
        if distance[y][x] < nowCost:
            continue
        for idx in range(4):
            nextX = x + nX[idx]
            nextY = y + nY[idx]
            if 0 <= nextX and nextX < n and 0 <= nextY and nextY < n:
                if nowCost + cave[nextY][nextX] < distance[nextY][nextX]:
                    distance[nextY][nextX] = nowCost + cave[nextY][nextX]
                    heappush(q,[nowCost + cave[nextY][nextX],(nextX,nextY)])
    print("Problem {0}: {1}" .format(cnt,distance[n-1][n-1]))

N = int(input())
cnt = 1
while N != 0:
    cave = []
    for _ in range(N):
        cave.append(list(map(int,input().split())))

    dijkstra(N)
    
    N = int(input())
    cnt += 1