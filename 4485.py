# 녹색 옷 입은 애가 젤다지?
import sys
from heapq import heappush,heappop
INF = int(1e9)
input = sys.stdin.readline
nX = [0,1,0,-1]
nY = [-1,0,1,0]

def dijkstra(n):
    distance = [[INF for _ in range(n)] for _ in range(n)]  # 각 좌표를 노드로 삼기위해 INF로 초기화
    distance[0][0] = cave[0][0] # 시작 좌표의 weight는 [0,0]에 놓여진 도둑루피값
    q = []
    heappush(q,[cave[0][0],(0,0)])  # 시작 위치의 weight와 좌표를 push

    while q:
        nowCost,nowPosition = heappop(q)
        x,y = nowPosition
        if distance[y][x] < nowCost:    # 우선순위 큐로 꺼내온 코스트가 앞서 저장된 값보다 크면 검사 스킵
            continue
        for idx in range(4):    # 사방 탐색 + 인접 노드들의 최솟값 비교 및 업데이트
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