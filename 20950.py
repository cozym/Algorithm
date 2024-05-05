# 미술가 미미
import sys
input = sys.stdin.readline

N = int(input())
P = []
for _ in range(N):
    r,g,b = map(int,input().split())
    P.append((r,g,b))
gom = list(map(int,input().split()))
res = 1000

def recur(idx, mixInfo):
    L = len(mixInfo)
    if L > 1:
        R,G,B = 0,0,0
        for r,g,b in mixInfo:
            R += r
            G += g
            B += b
        R //= L
        G //= L
        B //= L
        dif = abs(gom[0]-R) + abs(gom[1]-G) + abs(gom[2]-B)
        global res
        res = min(res,dif)
    if idx>=N or L >= 7:
        return
    recur(idx+1, mixInfo[:])
    mixInfo.append(P[idx])
    recur(idx+1, mixInfo[:])

recur(0,[])
print(res)