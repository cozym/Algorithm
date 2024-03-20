# 모든 순열
import sys

N = int(sys.stdin.readline())
res = [0 for i in range(N)]
used = [False for i in range(N)]

def recursion(idx,N):
    if idx==N:
        print(*res)
        return
    for j in range(N):
        if used[j]==True:
            continue
        used[j] = True
        res[idx] = j+1
        recursion(idx+1,N)
        used[j] = False

recursion(0,N)