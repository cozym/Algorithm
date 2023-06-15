# 카드 구매하기
import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
P = [0]+P
DP = [0 for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        DP[i] = max(DP[i],DP[i-j]+P[j])

print(DP[N])