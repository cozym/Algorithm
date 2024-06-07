# 배열 합치기
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
a,b = 0,0
res = []

for i in range(N+M):
    if a == N:
        res += B[b:M]
        break
    if b == M:
        res += A[a:N]
        break
    if A[a] > B[b]:
        res.append(B[b])
        b += 1
    else:
        res.append(A[a])
        a += 1
    
print(*res)