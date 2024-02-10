# 수 찾기
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())
ms = list(map(int,sys.stdin.readline().split()))

for m in ms:
    l,r = 0,len(A)
    while True:
        half = (l+r)//2
        if A[half]==m:
            print(1)
            break
        elif A[half] > m:
            r = half
        else:
            l = half+1
        if l>=r:
            print(0)
            break
