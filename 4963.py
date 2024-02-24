# 섬의 개수
import sys
input = sys.stdin.readline
from collections import deque

mx = [1,1,0,-1,-1,-1,0,1]
my = [0,1,1,1,0,-1,-1,-1]

def BFS(y,x):
    Q = deque()
    Q.append([y,x])
    visit[y][x] = True
    while len(Q) != 0:
        current = Q.popleft()
        for idx in range(8):
            nx = current[1] + mx[idx]
            ny = current[0] + my[idx]
            if 0 <= nx and nx < w and 0 <= ny and ny < h:
                if visit[ny][nx] == False and land[ny][nx] == 1:
                    visit[ny][nx] = True
                    Q.append([ny,nx])

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    land = []
    visit = []
    cnt = 0
    for _ in range(h):
        land.append(list(map(int,input().split())))
        visit.append([False for _ in range(w)])
    for i in range(h):
        for j in range(w):
            if visit[i][j] == False and land[i][j] == 1:
                cnt += 1
                BFS(i,j)
    print(cnt)