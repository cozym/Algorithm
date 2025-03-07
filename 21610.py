# 마법사 상어와 비바라기
import sys
input = sys.stdin.readline

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
board = []
next_board = []
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)
move_info = []
for _ in range(M):
    move_info.append(list(map(int, input().split())))

clouds = {(N-1,0), (N-1,1), (N-2,0), (N-2,1)}
next_clouds = []
def make_cloud():
    for d,s in move_info:
        move(d, s)

def move(d, s):
    global board, next_board, clouds, next_clouds
    next_clouds = set()
    for r, c in clouds:
        nr = (r + dr[d-1] * s) % N
        nc = (c + dc[d-1] * s) % N
        board[nr][nc] += 1              # 구름 옮기고 +1
        next_clouds.add((nr,nc))
    next_board = [row[:] for row in board]
    clouds = next_clouds
    next_clouds = set()
    for r, c in clouds:
        water_copy(r, c)                # +1 된 곳들 물복사마법
    board = next_board
    for i in range(N):
        for j in range(N):
            if (i, j) in clouds:        # 기존 구름 위치 체크
                continue
            if board[i][j] >= 2:        # 물 양 2 이상인 곳 구름 생성성
                board[i][j] -= 2
                next_clouds.add((i, j))
    clouds = next_clouds

def water_copy(r, c):
    diagonal_r = [-1, 1, 1, -1]
    diagonal_c = [1, 1, -1, -1]
    cnt = 0
    global next_board
    for i in range(4):
        nr = r + diagonal_r[i]
        nc = c + diagonal_c[i]
        if 0 <= nr < N and 0 <= nc < N: # 대각 경계 체크
            if board[nr][nc] != 0:
                cnt += 1
    next_board[r][c] += cnt

make_cloud()

print(sum(sum(r) for r in board))