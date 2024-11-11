# 거스름돈
import sys
input = sys.stdin.readline

n = int(input())
five = 0
two = 0
cnt = 0

while cnt*5 <= n:
    if (n-cnt*5)%2==0:
        five = cnt
        two = (n-five*5)//2
    cnt += 1

ans = five+two
print(ans if ans != 0 else -1)