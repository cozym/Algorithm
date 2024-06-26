# 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
point = [0]*100001

def bfs(n,k):
    q = deque()
    if n == 0:
        q.append(1)
    else:
        q.append(n)
    
    while q:
        x = q.popleft()
        if x==k:
            return point[x]

        for nx in (x-1,x+1,x*2):
            if 0 <= nx <= 100000 and point[nx]==0:
                if nx == 2*x:
                    point[nx] = point[x]
                    q.appendleft(nx)
                else:
                    point[nx] = point[x]+1
                    q.append(nx)

if N==0:
    if K==0:
        print(0)
    else:
        print(bfs(N,K)+1)
else :
    print(bfs(N,K))