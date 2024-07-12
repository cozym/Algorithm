# 가장 가까운 공통 조상
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    R = [[] for _ in range(N+1)]
    parent = [0]*(N+1)
    ancestors = []
    #depth = [0]*(N+1)

    for _ in range(N-1):
        a,b = map(int,input().split())
        R[a].append(b)
        parent[b] = a

    l,r = map(int,input().split())

    while l != 0:
        ancestors.append(l)
        l = parent[l]
    while r != 0:
        if r in ancestors:
            print(r)
            break
        r = parent[r]