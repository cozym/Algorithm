# 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    res = 0
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    idx_N,idx_M = N-1,M-1
    while idx_N >= 0 and idx_M >= 0:
        if A[idx_N] < B[idx_M]:
            idx_M -= 1
        elif A[idx_N] > B[idx_M]:
            res += idx_M+1
            idx_N -= 1
        else:
            idx_M -= 1
    print(res)