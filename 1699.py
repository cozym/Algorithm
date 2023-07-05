# 제곱수의 합
import sys

N = int(sys.stdin.readline())
count = 0

while N!=0:
    N -= int(N**0.5)**2
    count += 1

print(count)