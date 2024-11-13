# 밤양갱
import sys
input = sys.stdin.readline

N = int(input())
repeat = 1
cnt = 0

while repeat < N+1:
    cnt += 1
    repeat *= 2

if N==1:
    print(10)
else:
    print(8+cnt+1)