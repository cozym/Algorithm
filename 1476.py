# 날짜 계산
import sys

E,S,M = map(int,sys.stdin.readline().split())
day = 1

while True:
    e = day%15
    s = day%28
    m = day%19
    if day%15 == 0:
        e = 15
    if day%28 == 0:
        s = 28
    if day%19 == 0:
        m = 19
    if e==E and s==S and m==M:
        print(day)
        break
    day += 1