# 가장 긴 증가하는 부분 수열 4
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [1 for i in range(N)]
dp_list = []

for i in range(N):
    dp_list.append([A[i]])  # dp_list[i]를 A[i]로 초기화하여 default처리
    for j in range(i):
        if A[j]<A[i] and dp[j]+1>dp[i]:
            dp[i] = dp[j]+1
            dp_list[i] = dp_list[j]+[A[i]]  # A[i]로 끝나는 LIS원소들을 dp_list[i]에 초기화

M = max(dp)
print(M)
print(*dp_list[dp.index(M)])    # 최대 길이의 인덱스에 접근