# 태상이의 훈련소 생활
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ground = list(map(int,input().split()))
height = [0]*N

for _ in range(M):
    a,b,k = map(int,input().split())
    height[a-1] += k
    if b < N:
        height[b] -= k

ground[0] += height[0]
for i in range(1,N):
    height[i] += height[i-1]
    ground[i] += height[i]

print(*ground)