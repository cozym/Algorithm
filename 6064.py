# 카잉 달력
import sys

T = int(sys.stdin.readline())

for i in range(T):
    M,N,x,y = map(int,sys.stdin.readline().split())
    for date in range(x,M*N+x+1,M):
        if date%N==0:
            tmp_y = N
        else:
            tmp_y = date%N
        if tmp_y==y:
            print(date)
            break
    else:
        print(-1)