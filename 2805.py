# 나무 자르기
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
H = list(map(int,input().split()))
H.sort()

l,r = 1,H[-1]

while l <= r:
    sum = 0
    half = (l+r)//2
    for i in H:
        if i > half:
            sum += (i-half)
    if sum < M:
        r = half-1
    else:
        l = half+1

print(r)