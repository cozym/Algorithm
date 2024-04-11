# 연산자 끼워넣기
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
operators = list(map(int,input().split()))
maxRes = -int(1e9)
minRes = int(1e9)

def searchMaxMin(idx, n, add, sub, mul, div):
    global maxRes,minRes
    if idx == N:
        maxRes = max(maxRes,n)
        minRes = min(minRes,n)
        return
    
    if add:
        searchMaxMin(idx+1, n+A[idx], add-1, sub, mul, div)
    if sub:
        searchMaxMin(idx+1, n-A[idx], add, sub-1, mul, div)
    if mul:
        searchMaxMin(idx+1, n*A[idx], add, sub, mul-1, div)
    if div:
        searchMaxMin(idx+1, int(n/A[idx]), add, sub, mul, div-1)
    
searchMaxMin(1,A[0],operators[0],operators[1],operators[2],operators[3])
print(maxRes)
print(minRes)