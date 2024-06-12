# 숫자 카드
import sys
input = sys.stdin.readline

N = int(input())
numCards = list(map(int,input().split()))
M = int(input())
targets = list(map(int,input().split()))
res = []

numCards.sort()

for i in targets:
    l,r = 0, N-1
    ans = 0
    while l <= r:
        mid = (l+r)//2
        if numCards[mid] > i:
            r = mid - 1
        elif numCards[mid] == i:
            ans = 1
            break
        else:
            l = mid + 1
    res.append(ans)

print(*res)