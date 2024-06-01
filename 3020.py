# 개똥벌레
import sys
input = sys.stdin.readline

N,H = map(int,input().split())
top = [0]*(H+1) # 종유석
bot = [0]*(H+1) # 석순
height = [0]*(H+1) # 각 높이마다 뚫고 가야하는 장애물의 개수
res = 200001

# 종유석 / 석순 의 1~H개수 top > down으로 누적
for i in range(N):
    m = int(input())
    if i%2==0:
        bot[m] += 1
    else:
        top[m] += 1

for j in range(H-1,-1,-1):
    bot[j] += bot[j+1]
    top[j] += top[j+1]

# 각 높이마다 장애물 개수 계산
for h in range(1,H+1):
    height[h] = bot[h] + top[H-h+1]
    res = min(res,height[h])

height[0] = -1 # 장애물이 없는 경우 고려

print(res, height.count(res))