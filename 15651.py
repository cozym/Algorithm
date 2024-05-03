# N과 M (3)
import sys

N,M = map(int,sys.stdin.readline().split())

p = [0 for i in range(M)]

def recursion(idx):
    if idx==M:
        print(*p)
        return
    for i in range(1,N+1):
        p[idx] = i
        recursion(idx+1)

recursion(0)