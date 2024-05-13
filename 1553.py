# 도미노 찾기
import sys
input = sys.stdin.readline

domino = []
for l in range(7):
    for r in range(l,7):
        domino.append([l,r])
grid = []
for _ in range(8):
    line = []
    for i in input().rstrip():
        line.append(int(i))
    grid.append(line)

