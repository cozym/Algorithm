# 물약 구매
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
C = list(map(int,input().split()))
p = {}
res = 1e9

for i in range(1,N+1):
    p[i] = []
    for j in range(int(input())):
        a,d = map(int,input().split())
        p[i].append([a,d])

def calculate(l,c):
    priceAll = 0
    global res
    for d in l:
        priceAll += c[d-1]
        if priceAll > res:
            return
        for m in p[d]:
            c[m[0]-1] -= m[1]
            if c[m[0]-1] < 1:
                c[m[0]-1] = 1
    if priceAll < res:
        res = priceAll

check = permutations(range(1,N+1),N)

for l in list(check):
    calculate(l,C[:])

print(res)