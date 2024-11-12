# 게임을 만든 동준이
import sys
input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

cnt = 0
scores.reverse()

prev = scores[0]
for idx in range(1,N):
    if scores[idx] >= prev:
        cnt += (scores[idx] - prev + 1)
        scores[idx] = prev - 1
    prev = scores[idx]

print(cnt)