# 누가 이길까
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
HI = list(map(int,input().split()))
ARC = list(map(int,input().split()))
result = [0]*3

HI.sort()
ARC.sort()

# 해당 수와 가장 가까운 왼쪽, 오른쪽 인덱스 탐색 > 승,패,무 적립
for power in HI:
    l,r = 0,M-1
    left,right = 0,-1
    while l <= r:
        mid = (l+r)//2
        if ARC[mid] >= power:
            left = mid
            r = mid - 1
        else:
            l = mid + 1
    l,r = 0,M-1
    while l <= r:
        mid = (l+r)//2
        if ARC[mid] <= power:
            right = mid
            l = mid + 1
        else:
            r = mid - 1
    if power == ARC[right]:
        result[0] += left
        result[2] += right - left + 1
    else:
        result[0] += right+1

result[1] = M*N-(result[0]+result[2])
print(*result)