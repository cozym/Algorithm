# 기타콘서트
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
info = []
music = [False for _ in range(M)]
maxCan = [False for _ in range(M)]
res = 11
for _ in range(N):
    name, can = map(str,input().split())
    for i in range(M):
        if can[i]=='Y':
            maxCan[i] = True
    info.append((name,can))

def recursion(idx, music, cnt):
    if maxCan[:] == music[:]:
        global res
        res = min(res, cnt)
        return
    if idx >= N:
        return

    recursion(idx+1, music[:], cnt)
    for j in range(M):
        if info[idx][1][j] == 'Y':
            music[j] = True
    recursion(idx+1, music[:], cnt+1)

recursion(0, music, 0)

print(-1 if True not in maxCan else res)