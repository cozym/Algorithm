# 뒤집기
import sys
input = sys.stdin.readline

S = input().rstrip()
cnt = {'0' : 0 , '1' : 0}
now = '-1'

for c in S:
    if now != c:
        now = c
        cnt[now] += 1

print(min(cnt['0'], cnt['1']))