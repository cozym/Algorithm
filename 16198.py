import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))
used = [True] * N
ans = 0

def recur(w, e):
    l = len(w)
    if l == 2:
        global ans
        ans = max(ans, e)
        return
    
    for i in range(1, l-1):
        tmp = w[:]
        tmp.pop(i)
        recur(tmp, e + w[i-1] * w[i+1])

recur(W, 0)

print(ans)