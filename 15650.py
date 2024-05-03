# N과 M (2)
import sys

N,M = map(int,sys.stdin.readline().split())

pick = [0 for _ in range(M)]
used = [False for _ in range(N+1)]

def recursion(idx,start):
    if idx==M:
        print(*pick)
        return
    
    for i in range(start,N+1):
        if used[i]:
            continue
        pick[idx] = i
        used[i] = True
        recursion(idx+1,i+1)
        used[i] = False

recursion(0,1)