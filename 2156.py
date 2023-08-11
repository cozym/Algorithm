# 포도주 시식
import sys

n = int(sys.stdin.readline())
price = []  # 입력받는 포도주의 양 저장
dp = [[0,0] for i in range(n+1)]    # n번째 잔까지의 최대값
price.append(int(sys.stdin.readline()))
dp[1][0] = 0
dp[1][1] = price[0]

#dp[n][0] = dp[n-1][1]
#dp[n][1] = max(dp[n-2][0] + price[n-1] , dp[n-1][0]) + price[n]
for i in range(2,n+1):
    price.append(int(sys.stdin.readline()))
    dp[i][0] = dp[i-1][1]
    dp[i][1] = max(dp[i-2][0]+price[i-2], dp[i-1][0])+price[i-1]

print(max(dp[n]))