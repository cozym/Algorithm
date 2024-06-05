# 평균
import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int,input().split()))
M = max(scores)
res = 0
for s in scores:
    res += s/M*100

print(res/N)