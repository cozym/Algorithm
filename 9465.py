# 스티커
import sys

T = int(sys.stdin.readline())

# dp[n][x] = max(dp[n-1][y])+score[n]
# 0 <= x <= 2 , 0 : n번째 위 스티커 선택 / 1 : 아래 스티커 선택 / 2 : 안선택
# y는 x가 0일 경우 dp[n-1]의 모든 경우 고려 / 1,2일 경우 x외의 경우 고려
def max_score(n,scores):
    dp = [[0,0,0] for i in range(n)]
    dp[0][0] = scores[0][0]
    dp[0][1] = scores[1][0]
    dp[0][2] = 0
    for j in range(1,n):
        dp[j][0] = max(dp[j-1][1],dp[j-1][2])+scores[0][j]
        dp[j][1] = max(dp[j-1][0],dp[j-1][2])+scores[1][j]
        dp[j][2] = max(dp[j-1])
    print(max(dp[n-1]))

for t in range(T):
    scores = []
    n = int(sys.stdin.readline())
    scores.append(list(map(int,sys.stdin.readline().split())))
    scores.append(list(map(int,sys.stdin.readline().split())))
    max_score(n,scores)