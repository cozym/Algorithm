# 2차원 배열의 합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(M+1)]
presum = 0
for _ in range(N):
    row = list(map(int, input().split()))
    row = [0] + row
    for idx in range(1, M+1):
        row[idx] += row[idx-1]
    arr.append(row)

for r in range(1, N+1):
    for c in range(M+1):
        arr[r][c] += arr[r-1][c]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(arr[x][y] - arr[i-1][y] - arr[x][j-1] + arr[i-1][j-1])