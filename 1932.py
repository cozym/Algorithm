# 정수 삼각형
import sys

n = int(sys.stdin.readline())
dp = [] # 각 층까지의 최대값 담을 공간
dp.append([int(sys.stdin.readline())])  # 첫번째 층 사전처리

for i in range(1,n):
    scores = list(map(int,sys.stdin.readline().split()))
    dp.append([])
    for j in range(len(scores)):
        if j==0:
            dp[i].append(dp[i-1][j]+scores[j])  # n번째 줄 첫번째 원소 처리
        elif j==i:
            dp[i].append(dp[i-1][j-1]+scores[j])    # n번째 줄 마지막 원소 처리
        else:
            dp[i].append(max(dp[i-1][j-1],dp[i-1][j])+scores[j])    # 중간 원소들 처리

print(max(dp[n-1]))


