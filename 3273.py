# 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
x = int(input())
res = 0
a.sort()

l,r = 0,n-1

while l < r:
    s = a[l] + a[r]
    if s == x:
        res += 1
        l += 1
    if s > x:
        r -= 1
    elif s < x:
        l += 1

print(res)