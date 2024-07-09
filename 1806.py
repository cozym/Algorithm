# 부분합
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))
res = 100001

l,r,s = 0,0,0
while True:
    if s < S:
        if r >= N:  # 종료조건 위치 중요
            break
        s += arr[r]
        r += 1
    else:
        res = min(res,r-l)
        s -= arr[l]
        l += 1

print(res if res!=100001 else 0)