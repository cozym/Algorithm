# 1로 만들기
import sys

X = int(sys.stdin.readline())
res = 0

while X!=1:
    if X%3==0:
        X //= 3
    elif (X-1)%3==0:
        X -= 1
        X //= 3
        res += 1
    elif X%2==0:
        X //= 2
    else:
        X -= 1
    res += 1

print(res)