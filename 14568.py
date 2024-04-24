# 2017 연세대학교 프로그래밍 경시대회
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for teck in range(2,N+1,2):
    for young in range(1,N+1):
        for nam in range(young+2,N+1):
            if teck+young+nam == N:
                cnt += 1

print(cnt)