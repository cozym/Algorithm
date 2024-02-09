# 구간 합 구하기 5
import sys

N,M = map(int, sys.stdin.readline().split())
table = [[0]*(N+1)]

# 이차원 누적합 : 가로 > 세로 누적합
# 가로 누적합
for r in range(N):
    row = [0] + list(map(int,sys.stdin.readline().split()))
    for i in range(1,N+1):
        row[i] += row[i-1]
    table.append(row)

# 세로 누적합
for c in range(1,N+1):
    for i in range(1,N+1):
        table[i][c] += table[i-1][c]

print(table)

for i in range(M):
    res = 0
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1])