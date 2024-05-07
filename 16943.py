# 숫자 재배치
import sys
input = sys.stdin.readline

A,B = map(str,input().split())
B = int(B)
L = len(A)
num = [0 for _ in range(L)]
used = [False for _ in range(L)]
res = -1

def recur(idx):
    if idx==L:
        n = int(''.join(num))
        if n < B:
            global res
            res = max(res, n)
        return
    if num[0]=='0':
        return
    
    for i in range(L):
        if used[i]:
            continue
        used[i] = True
        num[idx] = A[i]
        recur(idx+1)
        used[i] = False

recur(0)
print(res)