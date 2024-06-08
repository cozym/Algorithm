# 가장 긴 짝수 연속한 부분 수열 (large)
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
S = list(map(int,input().split()))
l,r = 0,0
odd = 0
res = 0

while r < N:
    if odd <= K:
        if S[r]%2 != 0:
            odd += 1
        res = max(res, r-l-odd+1)
        r += 1
    else:
        if S[l]%2 != 0:
            odd -= 1
        l += 1

print(res)