# 숫자 정사각형
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rec = []
for _ in range(N):
    rec.append(input().rstrip())

ans = 0

for r in range(N):
    for c in range(M):
        L = 1
        while r+L < N and c+L < M:
            if rec[r][c] == rec[r][c+L] == rec[r+L][c] == rec[r+L][c+L]:
                ans = max(ans, L)
            L += 1

print((ans+1)**2)