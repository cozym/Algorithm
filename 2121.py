# 넷이 놀기
import sys
input = sys.stdin.readline

N = int(input())
w,h = map(int,input().split())
dots = set()
res = 0

for _ in range(N):
    x,y = map(int,input().split())
    dots.add((x,y))

for x,y in dots:
    if (x,y) in dots and (x+w,y) in dots and (x,y+h) in dots and (x+w,y+h) in dots:
        res += 1

print(res)