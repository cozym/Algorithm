# 대회 or 인턴
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
res = 0

for i in range(100):
    N -= 2
    M -= 1
    if N+M < K or N < 0 or M < 0:
        break
    res += 1

print(res)