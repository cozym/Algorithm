# 인간-컴퓨터 상호작용
import sys

countSum = {}
for i in range(ord('a'),ord('z')+1):
    countSum[chr(i)] = [0]

S = sys.stdin.readline()
q = int(sys.stdin.readline())

countSum[S[0]][0] += 1

for alphabet in range(1,len(S)-1):
    for i in countSum:
        if S[alphabet]==i:
            countSum[i].append(countSum[i][alphabet-1]+1)
        else:
            countSum[i].append(countSum[i][alphabet-1])

for i in range(q):
    a,l,r = sys.stdin.readline().split()
    l,r = int(l),int(r)
    if l==0:
        print(countSum[a][r])
    else:
        print(countSum[a][r]-countSum[a][l-1])