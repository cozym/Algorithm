# 스토쿠
import sys
input = sys.stdin.readline
# 0 좌표 파악
# 각 0에 1~9까지 대입
# 행, 열, 3*3 조건 check

checkIdx = [(0,1,2),(3,4,5),(6,7,8)]
zeroIdx = []
pad = []
for x in range(9):
    line = list(map(int,input().split()))
    pad.append(line)
    for y in range(9):
        if line[y] == 0:
            zeroIdx.append((x,y))

# def check():
#     for t in range(9):
#         col = [False for _ in range(10)]
#         row = [False for _ in range(10)]
#         for k in range(9):  # 행, 열 조건검사, 안맞으면 종료
#             c = pad[t][k]
#             r = pad[k][t]
#             if c != 0 and col[c]:
#                 return False
#             if r != 0 and row[r]:
#                 return False
#             col[c] = True
#             row[r] = True
    
#     for rs in checkIdx: # 3*3 조건검사
#         for cs in checkIdx:
#             square = [False for _ in range(10)]
#             for r in rs:
#                 for c in cs:
#                     n = pad[r][c]
#                     if n != 0 and square[n]:
#                         return False
#                     square[n] = True
#     return True

L = len(zeroIdx)
def recur(idx):
    # x,y = prex,prey
    for t in range(9):
        col = [False for _ in range(10)]
        row = [False for _ in range(10)]
        for k in range(9):  # 행, 열 조건검사, 안맞으면 종료
            c = pad[t][k]
            r = pad[k][t]
            if c != 0 and col[c]:
                return
            if r != 0 and row[r]:
                return
            col[c] = True
            row[r] = True

    for rs in checkIdx: # 3*3 조건검사
        for cs in checkIdx:
            square = [False for _ in range(10)]
            for r in rs:
                for c in cs:
                    n = pad[r][c]
                    if n != 0 and square[n]:
                        return
                    square[n] = True

    if idx == L:
        for line in pad:
            print(*line)
        exit()

    x,y = zeroIdx[idx]
    for i in range(1,10):
        pad[x][y] = i
        recur(idx+1)
        pad[x][y] = 0

recur(0)