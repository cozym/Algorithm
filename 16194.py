# 카드 구매하기 2
import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
DP = [-1 for i in range(N+1)]
P = [0]+P
DP[0]=0

for i in range(1,N+1):
    for j in range(1,i+1):
        if DP[i]==-1 or DP[i] > DP[i-j]+P[j]:
            DP[i] = DP[i-j]+P[j]

print(DP[N])