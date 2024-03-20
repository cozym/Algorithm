# 토마토
import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
storage = []
Q = deque()
mx = [1,0,-1,0]
my = [0,1,0,-1]
visit = [[False for _ in range(M)] for _ in range(N)]
res = 0

for _ in range(N):
    storage.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if storage[i][j] == 1:
            Q.append([i,j])

def BFS():
    while len(Q)!=0:
        global res
        res += 1
        l = len(Q)
        for cicle in range(l):
            current = Q.popleft()
            storage[current[0]][current[1]] = 1
            for move in range(4):
                nx = current[1] + mx[move]
                ny = current[0] + my[move]
                if 0 <= nx and nx < M and 0 <= ny and ny < N:
                    if visit[ny][nx] == False and storage[ny][nx] == 0:
                        Q.append([ny,nx])
                        visit[ny][nx] = True

BFS()
for i in range(N):
    for j in range(M):
        if storage[i][j] == 0:
            res = 0
print(res-1)