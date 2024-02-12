# 어두운 굴다리
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
x = list(map(int,input().split()))

res = x[0]
pre = 0
for i in x:
    middle = i+pre
    if middle%2==0:
        if middle//2-pre > res:
            res = middle//2-pre
    else:
        if (middle//2+1)-pre > res:
            res = (middle//2+1)-pre
    pre = i
else:
    if N-i > res:
        res = N-i

print(res)