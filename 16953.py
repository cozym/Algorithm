# A -> B
import sys
input = sys.stdin.readline

A,B = map(int,input().split())
res = int(1e9)

def recur(num, cnt):
    if num == B:
        global res
        res = min(res, cnt)
    if num > B:
        return
    recur(num*10+1, cnt+1)
    recur(num*2, cnt+1)

recur(A,0)

print(-1 if res == int(1e9) else res+1)