# 바이러스
import sys
input = sys.stdin.readline

n = int(input())
R = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

for _ in range(int(input())):
    a,b = map(int,input().split())
    R[a].append(b)
    R[b].append(a)

def dfs(node):
    visited[node] = True
    global cnt
    cnt += 1
    for next_node in R[node]:
        if visited[next_node]:
            continue
        dfs(next_node)

dfs(1)
print(cnt-1)