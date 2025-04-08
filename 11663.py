# 선분 위의 점
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dot = list(map(int, input().split()))
linedot = dot[:]
dot = set(dot)

line = []
last = 0
for _ in range(M):
    s,e = map(int, input().split())
    line.append([s,e])
    linedot.append(s)
    linedot.append(e)

linedot = sorted(set(linedot))

presum = {}
cnt = 0
for idx in range(len(linedot)):
    presum[linedot[idx]-1] = cnt
    if linedot[idx] in dot:
        cnt += 1
    presum[linedot[idx]] = cnt

for s, e in line:
    print(presum[e] - presum[s-1])