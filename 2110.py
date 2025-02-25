# 공유기 설치
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))

house.sort()
l,r = 1, house[N-1] - house[0]
d = 0

while l <= r:
    m = (l + r) // 2
    cnt = 1
    current = house[0]
    
    for idx in range(1, N):
        if current + m <= house[idx]:
            current = house[idx]
            cnt += 1
    
    if C <= cnt:
        l = m + 1
        d = m
    else:
        r = m - 1

print(d)