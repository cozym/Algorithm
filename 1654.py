# 랜선 자르기
import sys
input = sys.stdin.readline

K,N = map(int,input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
res = 0

l,r = 1,max(lines)
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for cm in lines:
        cnt += cm//mid
    if cnt < N:
        r = mid - 1
    else:
        res = mid
        l = mid + 1

print(res)