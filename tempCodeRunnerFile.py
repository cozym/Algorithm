# 보물섬
import sys
from collections import deque
input = sys.stdin.readline

h,w = map(int,input().split())
nx = [0,1,0,-1]
ny = [-1,0,1,0]
board = []
visited = [([True]*w) for _ in range(h)]
for _ in range(h):
    board.append(input().rstrip())
res = 0

def bfs(r,c):
    global localCnt,res
    q = deque()
    q.append((r,c))
    while q:
        L = len(q)
        for _ in range(L):
            x,y = q.popleft()
            for idx in range(4):
                nextX = x + nx[idx]
                nextY = y + ny[idx]
                if 0 <= nextX < h and 0 <= nextY < w:
                    if board[nextX][nextY]=='L' and visited[nextX][nextY]:
                        q.append((nextX,nextY))
                        visited[nextX][nextY] = False
        localCnt += 1   # bfs 한싸이클 돌때마다 depth + 1
    res = max(res,localCnt-1) # 가장 깊은 depth 저장

for r in range(h):
    for c in range(w):
        visited = [([True]*w) for _ in range(h)]
        localCnt = 0
        if board[r][c] == 'L':
            bfs(r,c)

print(res)