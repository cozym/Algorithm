# 카잉 달력
import sys

T = int(sys.stdin.readline())

for i in range(T):
    M,N,x,y = map(int,sys.stdin.readline().split())
    for date in range(1,40001):
        if date%M==0:
            tmp_x = M
        else:
            tmp_x = date%M
        if date%N==0:
            tmp_y = N
        else:
            tmp_y = date%N

        if tmp_x==x and tmp_y==y:
            print(date)
            break
        if tmp_x==M and tmp_y==N:
            print(-1)
            break