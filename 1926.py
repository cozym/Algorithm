# 그림
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n, m = map(int, input().split())
draw = []
for _ in range(n):
    draw.append(list(map(int, input().split())))

visited = [([True]*m) for _ in range(n)]
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def dfs(node):
    r, c = node
    visited[r][c] = False
    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]
        if 0 <= nr < n and 0 <= nc < m:
            if visited[nr][nc] and draw[nr][nc] == 1:
                visited[nr][nc] = False
                global area
                area += 1
                dfs((nr, nc))

cnt = 0
max_area = 0
for r in range(n):
    for c in range(m):
        if draw[r][c] == 1 and visited[r][c]:
            cnt += 1
            area = 1
            dfs((r, c))
            max_area = max(max_area, area)

print(cnt)
print(max_area)