# lifeguards
import sys
input = sys.stdin.readline

N = int(input())
times = []
guardTime = [0 for _ in range(1001)]
res = 1001
for _ in range(N):
    s,e = map(int,input().split())
    times.append((s,e))
    for t in range(s,e):
        guardTime[t] += 1

for s,e in times:
    tmp = guardTime[:]
    for t in range(s,e):
        tmp[t] -= 1
    res = min(res,tmp.count(0)-1)

print(1000-res)