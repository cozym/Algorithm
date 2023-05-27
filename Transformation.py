# 진법 변환 2745
import sys

n,b = sys.stdin.readline().split()
ans = 0

for i in n:
    if i>=65:
        r = ord(i)-55
    else:
        r = int(i)
    ans += r
    ans *= b

print(b,n)


7 // 2 = 3..1
3 // 2 = 1..1
1 // 2 = 0..1
