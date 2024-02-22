# 체스판 다시 칠하기 2
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
blackStart = []
whiteStart = []
blackStart.append(['B'])
whiteStart.append(['W'])
blackDiff = [[0]*(M+1)]
whiteDiff = [[0]*(M+1)]
res = 4000001

# B시작 체스판, W시작 체스판 첫줄 셋업
for i in range(1,M):
    if blackStart[0][i-1] == 'B':
        blackStart[0].append('W')
        whiteStart[0].append('B')
    else:
        blackStart[0].append('B')
        whiteStart[0].append('W')
# 나머지 체스판 셋업
for j in range(1,N):
    blackStart.append([])
    whiteStart.append([])
    for i in range(M):
        if blackStart[j-1][i] == 'B':
            blackStart[j].append('W')
            whiteStart[j].append('B')
        else:
            blackStart[j].append('B')
            whiteStart[j].append('W')

# 색칠해야하는 누적합 계산
for x in range(1,N+1):
    nowLine = input()
    blackDiff.append([0])
    whiteDiff.append([0])
    for y in range(1,M+1):
        blackDiff[x].append(blackDiff[x-1][y] + blackDiff[x][y-1] - blackDiff[x-1][y-1])
        whiteDiff[x].append(whiteDiff[x-1][y] + whiteDiff[x][y-1] - whiteDiff[x-1][y-1])
        if blackStart[x-1][y-1] != nowLine[y-1]:
            blackDiff[x][y] += 1
        else:
            whiteDiff[x][y] += 1

# 최솟값 도출
for x in range(K,N+1):
    for y in range(K,M+1):
        B = blackDiff[x][y] - blackDiff[x-K][y] - blackDiff[x][y-K] + blackDiff[x-K][y-K]
        W = whiteDiff[x][y] - whiteDiff[x-K][y] - whiteDiff[x][y-K] + whiteDiff[x-K][y-K]
        res = min(B,W,res)

print(res)