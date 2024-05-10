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

def checkRow(x,n):
    for k in range(9):  # 행 조건검사
        if pad[x][k] == n:
            return False
    return True

def checkCol(y,n):
    for k in range(9):  # 열 조건검사
        if pad[k][y] == n:
            return False
    return True

def checkBox(x,y,n):
    for ix in checkIdx: # 속한 3*3 위치파악
        if x in ix:
            a = ix
        if y in ix:
            b = ix

    for r in a: # 3*3 조건검사
        for c in b:
            if pad[r][c] == n:
                return False
    return True


L = len(zeroIdx)
def recur(idx):
    if idx == L:
        for line in pad:
            print(*line)
        exit()

    x,y = zeroIdx[idx]
    for i in range(1,10):
        if checkRow(x,i) and checkCol(y,i) and checkBox(x,y,i):
            pad[x][y] = i
            recur(idx+1)
            pad[x][y] = 0

recur(0)