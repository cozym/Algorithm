# 동물원
import sys

H = int(sys.stdin.readline())
# dp[n][x][y] : x,y좌표에 n마리를 배치하는 방법의 수
dp = [[[1,1] if j==0 else [0,0] for i in range(H)] for j in range(H)]

for nums in range(1,H):
    for x in range(H):
        for y in range(2):
            if x < H-1:
                dp[nums][x][y] = sum(dp[nums-1][x+1:H-nums])-dp[nums-1][x+1][0]


print(dp)
#for r in range(H):
