# 소가 길을 건너간 이유 5
import sys
input = sys.stdin.readline

N,K,B = map(int,input().split())
light = [True for _ in range(N+1)]

for _ in range(B):
    light[int(input())] = False

res = light[1:K+1].count(False)
for i in range(K+1,N+1):
    current = res
    if not light[i-K]:
        current -= 1
    if not light[i]:
        current += 1
    res = min(res, current)

print(res)