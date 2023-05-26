# 진법 변환2 11005
import sys

n,b = map(int,sys.stdin.readline().rstrip().split())
res = ""

while True:
    T = n%b
    if T >= 10 and T <= 35:
        res = chr(T+55)+res
    else:
        res = str(n%b)+res
    if n//b==0:
        break
    n //= b

print(res)