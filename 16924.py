# 십자가 찾기
import sys
input = sys.stdin.readline

# 한 칸씩 중심으로 잡고 사이즈 늘리면서 check
# 방문 체크하여 안된 곳 존재 시 -1
N, M = map(int, input().split())
grid = []

for r in range(N):
    row = []
    for e in input().rstrip():
        row.append(e)
    grid.append(row)

def check(r, c):
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]
    l = 1

    while True:
        con = True
        for i in range(4):
            nr = r + dr[i] * l
            nc = c + dc[i] * l
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                l -= 1
                con = False
                break
            elif grid[nr][nc] != '*' and grid[nr][nc] != '#':
                l -= 1
                con = False
                break
        if not con:
            break
        l += 1

    if l >= 1:
        grid[r][c] = '#'
        for i in range(1, l+1):
            for j in range(4):
                nr = r + dr[j] * i
                nc = c + dc[j] * i
                grid[nr][nc] = '#'

    return (l if l >= 1 else -1)

ans = []
for r in range(N):
    for c in range(M):
        if grid[r][c] == '*' or grid[r][c] == '#':
            L = check(r, c)
            if L >= 1:
                ans.append([r+1, c+1, L])

can = True
for row in grid:
    if '*' in row:
        can = False

if can:
    print(len(ans))
    for row in ans:
        print(*row)
else:
    print(-1)