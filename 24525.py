# SKK 문자열
import sys
input = sys.stdin.readline
INF = -1000000
S = input().rstrip()
prefixS = [0]
prefixK = [0]
res = -1
prefixSumIdx = {}
for i in range(-200001,200002):
    prefixSumIdx[i] = INF
prefixSumIdx[0] = 0

for i in range(1,len(S)+1):
    prefixS.append(prefixS[i-1])
    prefixK.append(prefixK[i-1])
    if S[i-1] == 'S':
        prefixS[i] += 1
    elif S[i-1] == 'K':
        prefixK[i] += 1
    now = 2*prefixS[i]-prefixK[i]   # 현재까지의 누적 S,K로 계산한 2*S - k
    if prefixSumIdx[now] == INF:    # 0이상의 2*S - K 값이 처음 나온다면 그 자리에 현재 인덱스 저장
        prefixSumIdx[now] = i
    else:
        if prefixK[i]-prefixK[prefixSumIdx[now]] >= 2 and prefixS[i]-prefixS[prefixSumIdx[now]] >= 1:    # 그 구간에 k가 2개 이상, s가 1개 이상인 경우만
            res = max(res, i - prefixSumIdx[now])   # 2*S - k가 앞서 나왔다면 거리 계산

print(res)
