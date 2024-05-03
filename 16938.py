# 캠프 준비
import sys
input = sys.stdin.readline

N,L,R,X = map(int,input().split())
A = list(map(int,input().split()))
res = 0

A.sort(reverse=True)

def recursion(idx, S, tmpA):
    if S > R:
        return
    if idx == N:
        if L <= S and S <= R and max(tmpA)-min(tmpA) >= X:
            global res
            res += 1
        return

    recursion(idx+1, S, tmpA[:])
    tmpA.append(A[idx])
    recursion(idx+1, S+A[idx], tmpA[:])

recursion(0,0,[])
print(res)