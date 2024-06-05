# 수들의 합 2
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
res = 0

l,r = 0,0
s = A[0]
while r < N:
    if s < M:
        r += 1
        if r == N:
            break
        s += A[r]
    elif s == M:
        res += 1
        s -= A[l]
        l += 1
    else:
        s -= A[l]
        l += 1

print(res)