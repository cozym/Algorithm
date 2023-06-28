# 가장 긴 증가하는 부분 수열 4
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [1 for i in range(N)]
dp_list = []

for i in range(N):
    dp_list.append([A[i]])
    for j in range(i):
        if A[j]<A[i] and dp[j]+1>dp[i]:
            dp[i] = dp[j]+1
            dp_list[i] = dp_list[j]+dp_list[i]
print(dp_list)


print(N,A)