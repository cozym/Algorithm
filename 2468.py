# 안전 영역
import sys
input = sys.stdin.readline

cnt = 0
area = []
visit = []

N = int(input())
for _ in range(N):
    area.append(list(map(int,input().strip().split())))
    visit.append([False]*N)

print(visit)