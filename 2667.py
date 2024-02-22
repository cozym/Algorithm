# 단지번호붙이기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)

nextX = [1,0,-1,0]
nextY = [0,1,0,-1]
map = []
visit = []
N = int(input())
count = 0
blockCount = 0
res = []

for _ in range(N):
    map.append(input().strip())
    visit.append([False]*N)

def countBlockDFS(x,y):
    visit[x][y] = True
    global blockCount
    blockCount += 1
    for idx in range(4):
        px = x + nextX[idx]
        py = y + nextY[idx]
        if 0 <= px and px < N and 0 <= py and py < N:
            if map[px][py] == '1' and visit[px][py] == False:
                countBlockDFS(px,py)

for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and visit[i][j] == False:
            count += 1
            countBlockDFS(i,j)
            res.append(blockCount)
            blockCount = 0
res.sort()
print(count)
for c in res:
    print(c)