# SKK 문자열
# s가 1개인 인덱스, k가 1개인 인덱스
import sys
input = sys.stdin.readline

S = input().strip()
prefixSumIdx = [0]*200010
prefixS = [0]
prefixK = [0]
res = -1

for i in range(1,len(S)+1):
    prefixS.append(prefixS[i-1])
    prefixK.append(prefixK[i-1])
    if S[i-1] == 'S':
        prefixS[i] += 1
    elif S[i-1] == 'K':
        prefixK[i] += 1
    now = prefixSumIdx[2*prefixS[i]-prefixK[i]]
    if prefixSumIdx[2*prefixS[i]-prefixK[i]] == 0:    # 2*S - K 값이 처음 나온다면
        prefixSumIdx[2*prefixS[i]-prefixK[i]] = i
    else:
        res = max(res, i - prefixSumIdx[2*prefixS[i]-prefixK[i]])   # 이미 해당 누적합값이 존재한다면 거리 계산

print(res)