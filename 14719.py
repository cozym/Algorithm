# 빗물
import sys
input = sys.stdin.readline

H,W = map(int,input().split())
world = [[0]*W for _ in range(H)]
blocks = list(map(int,input().split()))
res = 0

for c in range(W):
    for i in range(blocks[c]):
        world[i][c] = 1

for row in world:
    L = False   # 왼벽 초기화
    rain = 0
    for b in row:
        if b == 1:  # 벽을 만나면
            if L:   # 빗물 계산
                res += rain
            else:   # 왼벽 활성화
                L = True
            rain = 0
        elif b == 0:
            rain += 1

print(res)