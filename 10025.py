# 게으른 백곰
import sys
input = sys.stdin.readline
MAX_X = 1000001
N,K = map(int,input().split())
iceBucket = [0]*1000001

for _ in range(N):
    g,x = map(int,input().split())
    iceBucket[x] = g

maxIce = sum(iceBucket[:K*2+1])
nextIce = maxIce

for i in range(K*2+1,MAX_X):
    nextIce += (iceBucket[i] - iceBucket[i-(K*2+1)])
    if maxIce < nextIce:
        maxIce = nextIce

print(maxIce)