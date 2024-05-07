# 1,2,3 더하기 2
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
ans = ''
com = []

def recur(num):
    s = sum(num)
    if s > n:
        return
    if s == n:
        com.append(num)
        return

    num.append(1)
    recur(num[:])
    num.pop()
    num.append(2)
    recur(num[:])
    num.pop()
    num.append(3)
    recur(num[:])

recur([])
com.sort()

if k > len(com):
    print(-1)
else:
    for i in com[k-1]:
        ans+=str(i)
        ans+='+'
    print(ans[:-1])