# 용액
import sys
input = sys.stdin.readline

N = int(input())
ph = list(map(int,input().split()))
l,r = 0,N-1
res = [-1]*3

while l < r:
    s = ph[l] + ph[r]
    if res[2]==-1 or res[2] >= abs(s):
        res[2] = abs(s)
        res[0] = l
        res[1] = r
    if s >= 0:
        r -= 1
    else:
        l += 1

print(ph[res[0]],ph[res[1]])