# -2진수 (2089)
import sys

r = int(sys.stdin.readline())
ans = ''

if r==0:
    print('0')
    quit()

while r:
    if r%(-2):
        ans = '1'+ans
        r = r//(-2) + 1
    else:
        ans = '0'+ans
        r = r//(-2)

print(ans)