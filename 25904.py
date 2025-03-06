# 안녕 클레오파트라 세상에서 제일가는 포테이토칩
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
T = list(map(int, input().split()))

idx = 0
while True:
    if T[idx] < X:
        print(idx + 1)
        break
    idx = (idx + 1) % N
    X += 1