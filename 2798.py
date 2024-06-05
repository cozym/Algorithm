# 블랙잭
from itertools import combinations
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
cards = list(map(int,input().split()))
res = 300000

for three in list(combinations(cards,3)):
    S = sum(three)
    if M >= S:
        res = min(res, M-S)
        
print(M-res)