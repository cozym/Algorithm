# 진법 변환 2745
import sys

n,b = sys.stdin.readline().split()
ans = 0

for i,num in enumerate(reversed(n)):
    if ord(num)>=65:
        r = int(ord(num)-55)
    else:
        r = int(num)
    ans += r*(int(b)**i)

print(ans)