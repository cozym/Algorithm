# 점프 점프
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
s = int(input())
visited = [True] * n

def dfs(node):
    visited[node] = False

    r = node + A[node]
    l = node - A[node]
    if 0 <= r < n and visited[r]:
        dfs(r)

    if 0 <= l < n and visited[l]:
        dfs(l)

dfs(s-1)

print(visited.count(False))