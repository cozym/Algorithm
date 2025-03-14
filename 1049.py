# 기타줄
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = 0
pakage = float("inf")
each = float("inf")

for _ in range(M):
    six, one = map(int, input().split())
    pakage = min(pakage, six)
    each = min(each, one)

ans = pakage * (N // 6) + each * (N % 6)
ans = min(ans, pakage * ((N // 6) + 1), each * N)

print(ans)