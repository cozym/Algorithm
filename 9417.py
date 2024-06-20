# 최대 gcd
import sys
from itertools import combinations
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

for _ in range(int(input())):
    res = 0
    nums = list(map(int,input().split()))
    for a,b in list(combinations(nums,2)):
        res = max(res,gcd(a,b))
    print(res)