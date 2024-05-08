# 매직 스퀘어로 변경하기
import sys
input = sys.stdin.readline

used = [False for _ in range(10)]
checkIdx = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
arr = []
for _ in range(3):
    for i in list(map(int,input().split())):
        arr.append(i)
res = 100

square = [0 for _ in range(9)]
def recur(idx):
    lineS = 0
    for c in checkIdx:
        s = 0
        for j in c:
            if square[j] == 0:
                break
            s += square[j]
        else:
            if lineS == 0:
                lineS = s
            else:
                if lineS != s:
                    return
    
    cost = 0
    for i in range(9):
        if square[i] != 0:
            cost += abs(square[i]-arr[i])
    global res
    if cost > res:
        return

    if idx == 9:
        res = min(res, cost)
        return
    
    for i in range(1,10):
        if used[i]:
            continue
        used[i] = True
        square[idx] = i
        recur(idx+1)
        used[i] = False
    
recur(0)

print(res)