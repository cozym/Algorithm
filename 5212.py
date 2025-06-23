# 지구 온난화
import sys
input = sys.stdin.readline
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

R, C = map(int, input().split())

map_b = []

for _ in range(R):
    map_b.append(input().rstrip())

def check(r, c):
    if map_b[r][c] == '.':
        return '.'
    sea = 0
    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            sea += 1
        elif map_b[nr][nc] == '.':
            sea += 1
    return ('.' if sea >= 3 else 'X')

map_a = []
min_r, min_c = R, C
max_r, max_c = 0, 0
for r in range(R):
    row = []
    for c in range(C):
        cur = check(r, c)
        if cur == 'X':
            min_r = min(r, min_r)
            min_c = min(c, min_c)
            max_r = max(r, max_r)
            max_c = max(c, max_c)
        row.append(cur)
    map_a.append(row)

for r in range(min_r, max_r+1):
    print(''.join(map_a[r][min_c:max_c+1]))