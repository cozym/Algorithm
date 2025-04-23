# 공포의 면담실
import sys
input = sys.stdin.readline

totals = []
for _ in range(int(input())):
    totals.append(sum(list(map(int, input().split()))[1:]))

totals.sort()

for idx in range(1, len(totals)):
    totals[idx] += totals[idx - 1]

print(sum(totals))