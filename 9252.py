# LCS 2
import sys
input = sys.stdin.readline

str_1 = input().strip()
str_2 = input().strip()
dp = [[0,0] for _ in range(len(str_1))]
ans = 0

# 해당 인덱스를 포함하며 가장 긴 수열
# 이전 인덱스를 순회하며 마지막 인덱스 이후에 해당 인덱스값이 존재하는지 검사
# 더 큰 값이 나오면 업데이트 (길이,마지막 인덱스 저장)

for idx in range(len(str_1)):
    dp[idx] = [1,str_2.find(str_1[idx])]
    if dp[idx][1] == -1:
        dp[idx][0] = 0
        continue
    for frontIdx in range(idx):
        if dp[frontIdx][0] + 1 > dp[idx][0]:
            lastIdx = dp[frontIdx][1]
            backIdx = str_2[lastIdx+1:].find(str_1[idx])
            if backIdx != -1:
                dp[idx] = [dp[frontIdx][0]+1,lastIdx+backIdx+1]
    ans = max(ans,dp[idx][0])

print(ans)
print(dp)