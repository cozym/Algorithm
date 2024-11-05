# 나이트의 이동
import sys
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
move = 0
visited = []

def bfs(start, end, l):
    q = deque()
    q.append(start)
    global move
    sx, sy = start
    ex, ey = end
    visited[sx][sy] = False
    if sx == ex and sy == ey:
        return 0
    while q:
        L = len(q)
        move += 1
        for _ in range(L):
            cx, cy = q.popleft()
            for idx in range(8):
                nx = cx + dx[idx]
                ny = cy + dy[idx]
                if nx == ex and ny == ey:
                    return move
                if 0 <= nx < l and 0 <= ny < l:
                    if visited[nx][ny]:
                        visited[nx][ny] = False
                        q.append([nx,ny])


for T in range(int(input())):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [([True]*l) for _ in range(l)]
    move = 0
    print(bfs([sx,sy], [ex,ey], l))