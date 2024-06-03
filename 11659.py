# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
prefixSum = []
prefixSum.append(0)
for n in range(1,N+1):
    prefixSum.append(prefixSum[n-1]+nums[n-1])

for _ in range(M):
    i,j = map(int,input().split())
    print(prefixSum[j]-prefixSum[i-1])