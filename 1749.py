# 점수 따먹기
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
matrix = []
matrix.append([0]*(M+1))
res = int(-1e9)
for _ in range(N):
    line = [0]
    for n in list(map(int,input().split())):
        line.append(n)
    matrix.append(line)

# 이차원 누적합
for i in range(1,N+1):
    for j in range(1,M+1):
        matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        for r in range(i):
            for c in range(j):
                res = max(res, matrix[i][j] - matrix[r][j] - matrix[i][c] + matrix[r][c])

print(res)