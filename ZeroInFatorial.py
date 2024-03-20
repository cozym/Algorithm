# 팩토리얼 0의 개수 1676
import sys

N = int(sys.stdin.readline())
c = 0

for i in range(1,N+1):
    while(i%5==0):
        c += 1
        i //= 5

print(c)