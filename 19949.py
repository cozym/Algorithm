# 영재의 시험
import sys
input = sys.stdin.readline

answer = list(map(int,input().split()))
numSequence = [0 for _ in range(6)]
res = 0

def recursion(idx, cnt, yj):
    if idx == 10:
        if cnt >= 5:
            global res
            res += 1
        return
    
    for i in range(1,6):
        correct = cnt
        if answer[idx]==i:
            correct += 1
        if idx < 2 or (yj[idx-1] != i or yj[idx-2] != i):
            yj.append(i)
            recursion(idx+1,correct,yj)
            yj.pop()

recursion(0,0,[])
print(res)