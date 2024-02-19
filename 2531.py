# 회전 초밥
import sys
from collections import deque
input = sys.stdin.readline

N,d,k,c = map(int,input().split())
pick = deque()
res = 0
kdish = []

for _ in range(k):
    i = int(input())
    pick.append(i)
    kdish.append(i)

res = len(set(pick))
if c not in pick:
    res += 1

for _ in range(k,N):
    pick.popleft()
    pick.append(int(input()))
    tmp = set(pick)
    if len(tmp) >= res:
        res = len(tmp)
        if c not in tmp:
            res += 1

for i in range(k):
    pick.popleft()
    pick.append(kdish[i])
    tmp = set(pick)
    if len(tmp) >= res:
        res = len(tmp)
        if c not in tmp:
            res += 1

print(res)