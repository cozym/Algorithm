# 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
home = []
chicken = []
res = 1e9
for x in range(N):
    line = list(map(int,input().split()))
    for y in range(N):
        if line[y] == 1:
            home.append((x,y))
        elif line[y] == 2:
            chicken.append((x,y))

def findCityDistance(chickenGroup):
    citySum = 0
    global res
    for hx,hy in home:
        d = 200
        for cx,cy in chickenGroup:
            d = min(d,(abs(hx-cx) + abs(hy-cy)))
        citySum += d
        if citySum > res:
            break
    res = min(citySum,res)

ch = combinations(chicken,M)

for c in list(ch):
    findCityDistance(c)

print(res)