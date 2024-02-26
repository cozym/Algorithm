# 안전 영역
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

low,high,waterHigh = 100,0,0
cnts = []
area = []
mx = [1,0,-1,0]
my = [0,1,0,-1]

N = int(input())
for i in range(N):
    area.append(list(map(int,input().strip().split())))
    low = min(area[i]+[low])
    high = max(area[i]+[high])

def DFS(y,x):
    visit[y][x] = True
    for idx in range(4):
        nx = x + mx[idx]
        ny = y + my[idx]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if visit[ny][nx] == False and area[y][x] > waterHigh:
                DFS(ny,nx)

for w in range(low-1,high+2):
    waterHigh = w
    visit = [([False]*N) for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if visit[y][x] == False and area[y][x] > waterHigh:
                DFS(y,x)
                cnt += 1
    cnts.append(cnt)

print(max(cnts))