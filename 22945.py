# 팀 빌딩
import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int,input().split()))
res = 0

l,r = 0, N-1

while l < r:
    res = max(res, (r-l-1) * min(x[l],x[r]))
    if x[l] < x[r]:
        l += 1
    else:
        r -= 1

print(res)