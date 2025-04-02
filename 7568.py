# 덩치
import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    w, h = map(int, input().split())
    info.append([w,h])

ans = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            cnt += 1
    ans.append(cnt)

print(*ans)