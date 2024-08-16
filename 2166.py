# 다각형의 면적
# 벡터의 외적, 신발끈 공식
# https://o773h.tistory.com/36
import sys
input = sys.stdin.readline

x_dots = []
y_dots = []
N = int(input())
for _ in range(N):
    x,y = map(int,input().split())
    x_dots.append(x)
    y_dots.append(y)

x_dots.append(x_dots[0])
y_dots.append(y_dots[0])

front, back = 0,0
for idx in range(N):
    front += x_dots[idx]*y_dots[idx+1]
    back += y_dots[idx]*x_dots[idx+1]

ans = abs(front - back)*0.5
print(ans)