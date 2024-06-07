# 다이어트
# 1 2 3 4 5 6 7 8 9 10

# 1-1 = 1
# 4-1 = 3
# 9-1 = 8
# 16-1 = 15
# 25-1 = 24
# 25-4 = 21
# 25-9 = 16
# 25-16 = 9

# 36-1 = 35
# 36-4 = 32
# 36-9 = 27
# 36-16 = 20
# 36-25 = 11
import sys
input = sys.stdin.readline

G = int(input())
l,r = 1,1
cnt = 0

while r <= 100000:
    m = r**2-l**2
    if m < G:
        r += 1
    elif m == G:
        print(r)
        cnt += 1
        r += 1
    else:
        l += 1

if cnt==0:
    print(-1)