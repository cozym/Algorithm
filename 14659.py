# 한조서열정리하고옴ㅋㅋ
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = 0
now = 0

sequence = 0
for m in arr:
    if m > now:
        now = m
        sequence = 0
    else:
        sequence += 1
        ans = max(ans, sequence)

print(ans)