# 수들의 합
import sys
input = sys.stdin.readline

S = int(input())

step = 0
sum = 0
while sum <= S:
    step += 1
    sum += step

print(step - 1)