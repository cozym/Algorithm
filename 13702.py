# 이상한 술집
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
capacity = []
for _ in range(N):
    capacity.append(int(input()))
res = 0

l,r = 1,max(capacity)
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for m in capacity:
        cnt += m//mid
    if cnt < K: # mid를 줄여서 cnt를 늘려야한다
        r = mid - 1
    else:
        res = mid
        l = mid + 1

print(res)