# 연결 요소의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N,M = map(int,input().split())
R = [[] for _ in range(N+1)]
visit = [False]*(N+1)
res = 0

for _ in range(M):
    u,v = map(int,input().split())
    R[u].append(v)
    R[v].append(u)

def DFS(node):
    visit[node] = True
    for nextNode in R[node]:
        if visit[nextNode] == False:
            DFS(nextNode)

for idx in range(1,N+1):
    if visit[idx] == False:
        res += 1
        DFS(idx)

print(res)