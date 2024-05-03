# N과 M (4)
import sys

N,M = map(int,sys.stdin.readline().split())

p = [0 for i in range(M)]

def recursion(idx,start):
    if idx==M:
        print(*p)
        return
    for i in range(start,N+1):
        p[idx] = i
        recursion(idx+1,i)

recursion(0,1)