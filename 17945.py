# 통학의 신
import sys
input = sys.stdin.readline

A,B = map(int, input().split())

for x in range(-1000,1001):
    if x*x + 2*A*x + B == 0:
        print(x, end=' ')