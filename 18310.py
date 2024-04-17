# 안테나
import sys
input = sys.stdin.readline

N = int(input())
houses = list(map(int,input().split()))
res = 0
m = 1e9
        

aver = sum(houses)//N

for i in houses:
    if m > abs(aver-i):
        m = aver-i

print(res)