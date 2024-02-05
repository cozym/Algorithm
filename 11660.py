# 구간 합 구하기 5
import sys

N,M = map(int, sys.stdin.readline().split())
table = []

for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    for i in range(1,N):
        row[i] += row[i-1]
    table.append(row)

for i in range(M):
    res = 0
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for x in range(x1-1,x2):
        if y1==1:
            res += table[x][y2-1]
        else:
            res += (table[x][y2-1] - table[x][y1-2])
    print(res)