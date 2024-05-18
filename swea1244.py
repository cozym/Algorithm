# 최대 상금
from itertools import permutations
T = int(input())

def recur(idx):
    if idx == change:
        global res
        res = max(res, int(''.join(numArr)))
        return
    for i in range(L-1):
        for j in range(i+1,L):
            numArr[i],numArr[j] = numArr[j],numArr[i]
            tmp = ''.join(numArr)
            if dp[(change-idx-1,tmp)] == -1:    # 첫 방문 시
                recur(idx+1)
            dp[(change-idx-1,tmp)] = 1  # 방문 체크
            numArr[i],numArr[j] = numArr[j],numArr[i]

for test_case in range(1, T + 1):
    num, change = map(str,input().split())
    numArr = []
    for i in num:
        numArr.append(i)
    change = int(change)
    L = len(numArr)
    res = 0
    dp = {}
    for i in list(permutations(numArr,len(numArr))):
        tmp = ''.join(i)
        for cnt in range(change+1):
            dp[(cnt,tmp)] = -1

    recur(0)

    print("#{} {}".format(test_case,res))