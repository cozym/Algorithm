# 보석 상자
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
gems = []
for _ in range(M):
    gems.append(int(input()))

l,r = 1,max(gems)
res = 0

while l <= r:
    mid = (l+r)//2
    cnt = 0
    for color in gems:  # O(M)
        cnt += color // mid + (0 if color % mid == 0 else 1)
    if cnt > N: # (현재 질투심으로 계산한 학생 수 > 주어진 학생 수) 인 경우 l을 mid로 땡겨와 질투심을 늘려줌
        l = mid + 1
    else:   # 주어진 학생 수 이하가 나온다면 해당 질투심을 저장해두고 r을 mid로 땡겨와 질투심 최솟값을 탐색
        res = mid
        r = mid - 1

print(res)