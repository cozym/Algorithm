# 적어도 대부분의 배수
import sys
from itertools import combinations
input = sys.stdin.readline

nums = list(map(int,input().split()))
res = 1e10

def lcm(x,y):
    m = x*y
    while y!=0:
        x,y = y,x%y
    return m//x

combi = combinations(nums,3)
for a,b,c in list(combi):
    res = min(res,lcm(lcm(a,b),c))

print(res)