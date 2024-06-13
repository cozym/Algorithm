# 숫자 카드 2
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))
res = []
cards.sort()

for k in nums:
    l,r = 0,N-1
    left = -1
    while l <= r:
        mid = (l + r) // 2
        if cards[mid] < k:
            l = mid + 1
        elif cards[mid] == k:
            r = mid - 1
            left = mid
        else:
            r = mid - 1
    
    l,r = left,N-1
    right = -2
    while l <= r:
        mid = (l + r) // 2
        if cards[mid] < k:
            l = mid + 1
        elif cards[mid] == k:
            l = mid + 1
            right = mid
        else:
            r = mid - 1

    res.append(right-left+1)

print(*res)