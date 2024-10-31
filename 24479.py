# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

N,M,S = map(int,input().split())
visited = [True]*(N+1)
R = [[] for _ in range(N+1)]
ans = [0]*(N+1)
turn = 1

def dfs(node):
    global turn
    visited[node] = False
    ans[node] = turn
    for next_node in R[node]:
        if visited[next_node]:
            turn += 1
            dfs(next_node)

for _ in range(M):
    u,v = map(int, input().split())
    R[u].append(v)
    R[v].append(u)

for node in range(1,N+1):
    R[node].sort()

dfs(S)

for idx in range(1,N+1):
    print(ans[idx])