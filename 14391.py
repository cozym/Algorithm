# 종이 조각
import sys

N,M = map(int,sys.stdin.readline().split(" "))
piece = []

for i in range(N):
    piece.append(list(map(int,sys.stdin.readline().split())))

print(N,M,piece)