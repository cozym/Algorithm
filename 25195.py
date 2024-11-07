# Yes or yes
import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

N, M = map(int, input().split())
R = [[] for _ in range(N+1)]
visited = [True]*(N+1)
ans = "Yes"
for _ in range(M):
    u,v = map(int, input().split())
    R[u].append(v)
S = int(input())
arr_s = list(map(int,input().split()))

def dfs(node):
    visited[node] = False
    if len(R[node])==0:
        global ans
        ans = "yes"
        return
    for next_node in R[node]:
        if visited[next_node] and next_node not in arr_s:
            dfs(next_node)

dfs(1)

if 1 in arr_s:
    ans = "Yes"

print(ans)