# 징검다리
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    l,r = 0,N
    while l <= r:
        m = (l + r) // 2
        if ((m*(m+1)//2) + (m+1)) > N:
            r = m-1
        else:
            l = m+1
    print(l)