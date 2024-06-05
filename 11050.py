# 이항 계수
import sys
from itertools import combinations
input = sys.stdin.readline

N,K = map(int,input().split())
print(len(list(combinations(range(N),K))))