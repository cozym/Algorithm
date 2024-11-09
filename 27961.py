# 고양이는 많을수록 좋다
import sys
input = sys.stdin.readline

N = int(input())
cnt = 1
cats = 1

while cats < N:
    cats *= 2
    cnt += 1

if N == 0:
    cnt = 0

print(cnt)