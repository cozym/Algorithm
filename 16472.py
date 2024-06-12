# 고냥이
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
alpha = {}
c = deque()
res = 0
for i in range(26):
    alpha[chr(ord('a')+i)] = 0

l,r = 0,0
alpha[s[0]] += 1
while r < len(s):
    cnt = 0
    for i in range(26):
        if alpha[chr(ord('a')+i)] > 0:
            cnt += 1
    if cnt <= n:
        res = max(res, r-l+1)
        r += 1
        if r == len(s):
            break
        alpha[s[r]] += 1
    else:
        alpha[s[l]] -= 1
        l += 1

print(res)