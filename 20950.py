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
    if L > 1:   # 물감을 단독으로 사용 못하도록 필터링
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
    if idx>=N or L >= 7:    # 섞을 수 있는 최대 물감의 개수를 7개로 제한
        return
    recur(idx+1, mixInfo[:])    # 현재 물감을 안섞는경우
    mixInfo.append(P[idx])
    recur(idx+1, mixInfo[:])    # 현재 물감을 섞는경우

recur(0,[])
print(res)