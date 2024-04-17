# 편의점 2
import sys
input = sys.stdin.readline

n = int(input())
xs = []
ys = []
res = 0

for _ in range(n):
    x,y = map(int,input().split())
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

px = xs[n//2]
py = ys[n//2]

for i in range(n):
    res += abs(xs[i]-px)
    res += abs(ys[i]-py)

print(res)