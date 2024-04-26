# 색종이
import sys
input = sys.stdin.readline

n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    a,b = map(int,input().split())
    for x in range(a,a+10):
        for y in range(b,b+10):
            paper[x][y] += 1

zeroCnt = 0
for i in range(100):
    zeroCnt += paper[i].count(0)

print(10000-zeroCnt)