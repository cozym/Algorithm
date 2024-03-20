# 숫자판 점프
import sys
input = sys.stdin.readline

moveX = [1,0,-1,0]
moveY = [0,1,0,-1]
res = []
pad = []

for _ in range(5):
    pad.append(list(map(str,input().strip().split())))

def DFS(x,y,num):
    if len(num)==6:
        res.append(int(num))
        return
    for i in range(4):
        nextX = x+moveX[i]
        nextY = y+moveY[i]
        if 0 <= nextX and nextX < 5 and 0 <= nextY and nextY < 5:
            DFS(nextX,nextY,num+pad[nextX][nextY])

for i in range(5):
    for j in range(5):
        DFS(i,j,pad[i][j])

print(len(set(res)))