# 과일 서리
import sys
from math import comb
from itertools import combinations_with_replacement
input = sys.stdin.readline

N = int(input())
M = int(input())
# n+r-1 C r
# n = N / r = M-N
print(comb(M-1, M-N))
#print(len(list(combinations_with_replacement(range(N), M-N))))

# N가지 종류의 과일 중 M개를 훔친다

# 1 2 3
# 5개
# 1 1 1 1 1
# 1 1 1 1 2

# N개의 종류 중에서 (M - N)