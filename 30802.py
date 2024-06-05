# 웰컴 키트
import sys
from math import ceil
input = sys.stdin.readline

N = int(input())
sizeCnt = list(map(int,input().split()))
T,P = map(int,input().split())
resT = 0

for s in sizeCnt:
    resT += ceil(s/T)
    
print(resT)
print(N//P,N%P)